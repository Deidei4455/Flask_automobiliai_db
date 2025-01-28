from models import db, Automobil
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automobiliai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    search_text = request.args.get("search")
    if search_text:
        filtered_rows = (Automobil.query.filter
                         (Automobil.make.ilike(f"%{search_text}%")))
        all_prices = []
        all_years = []
        for car_row in filtered_rows:
            all_prices.append(car_row.price)
            all_years.append(car_row.year)
        price_sum = sum(all_prices)
        avg_year = int(round(sum(all_years) / len(all_years)))
        return (render_template
                ("all_cars_main.html", cars=filtered_rows, price_sum=price_sum, avg_year=avg_year))

    else:
        all_cars = Automobil.query.all()
        all_prices = []
        all_years = []
        for car_row in all_cars:
            all_prices.append(car_row.price)
            all_years.append(car_row.year)
        price_sum = sum(all_prices)
        avg_year = int(round(sum(all_years) / len(all_years)))
        return (render_template
                ("all_cars_main.html", cars=all_cars, price_sum=price_sum, avg_year=avg_year))


@app.route("/vehicle/<int:row_id>")
def one_car(row_id):
    car = Automobil.query.get(row_id)
    if car:
        return render_template("one_car.html", car=car)
    else:
        return f"Cars with id {row_id} were not found"


@app.route("/vehicle/new", methods=["GET", "POST"])
def new_vehicle():
    if request.method == "GET":
        return render_template("new_car.html")
    if request.method == "POST":
        make = request.form.get("make")
        model = request.form.get("model")
        color = request.form.get("color")
        year = int(request.form.get("year"))
        price = float(request.form.get("price"))
        fuel = request.form.get("fuel")
        if make:
            new_car = Automobil(make=make.title(), model=model,
                                color=color.lower(), year=year,
                                price=price, fuel_type=fuel.lower())
            db.session.add(new_car)
            db.session.commit()
        return redirect(url_for("home"))


@app.route("/vehicle/edit/<int:row_id>", methods=["get", "post"])
def update_project(row_id):
    car = Automobil.query.get(row_id)
    if not car:
        return f"Car with id {row_id} was not found"

    if request.method == "GET":
        return render_template("edit_car.html", car=car)

    elif request.method == "POST":
        make = request.form.get("make")
        model = request.form.get("model")
        color = request.form.get("color")
        year = int(request.form.get("year"))
        price = float(request.form.get("price"))
        fuel = request.form.get("fuel")
        if make:
            car.make = make
        if model:
            car.model = model
        if color:
            car.color = color
        if year:
            car.year = year
        if price:
            car.price = price
        if fuel:
            car.fuel_type = fuel
        db.session.commit()
        return redirect(url_for("home"))


@app.route("/vehicle/delete/<int:row_id>", methods=["POST"])
def delete_project(row_id):
    car = Automobil.query.get(row_id)
    if not car:
        return f"Vehicle with id {row_id} was not found"
    else:
        db.session.delete(car)
        db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()
