from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class Automobil(db.Model):
    __tablename__ = "automobiliai"
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String)
    model = db.Column(db.String)
    color = db.Column(db.String)
    year = db.Column(db.Integer)
    price = db.Column(db.Float)
    fuel_type = db.Column(db.String)
    date_created = db.Column(db.Date, default=datetime.date.today())

