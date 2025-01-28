from models import db, Automobil
from app import app

with app.app_context():
    autos = [
        Automobil(make="Audi", model="A4", color="black", year=2012, price=7000, fuel_type="petrol"),
        Automobil(make="Audi", model="A6", color="black", year=2013, price=9500, fuel_type="diesel"),
        Automobil(make="BMW", model="535", color="blue", year=2012, price=9000, fuel_type="diesel"),
        Automobil(make="Toyota", model="Yaris", color="silver", year=2004, price=1900, fuel_type="petrol"),
        Automobil(make="Mazda", model="323", color="brown", year=1999, price=1600, fuel_type="petrol"),
        Automobil(make="Mazda", model="6", color="red", year=2016, price=8600, fuel_type="diesel"),
        Automobil(make="Nissan", model="skyline", color="silver", year=2001, price=43000, fuel_type="petrol"),
        Automobil(make="Honda", model="Integra", color="yellow", year=2003, price=17000, fuel_type="petrol"),
        Automobil(make="Dodge", model="Charger", color="black", year=1969, price=130000, fuel_type="petrol"),
        Automobil(make="Dodge", model="Charger", color="green", year=2017, price=16000, fuel_type="petrol"),
        Automobil(make="Chevrolet", model="Camaro", color="gold", year=2012, price=12000, fuel_type="petrol"),
        Automobil(make="Ford", model="GT", color="red", year=2005, price=256000, fuel_type="petrol")
    ]

    db.session.add_all(autos)
    db.session.commit()
    print("Created autos")
