import random
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Products(db.Model):
    __tablename__= "Products"
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), unique=False, nullable=False)
    Price = db.Column(db.Float, unique=False, nullable=False)
    Color = db.Column(db.String(20), unique=False, nullable=False)


    
def seedData(db):
    color = ["BLue","Green", "Yellow", "Red", "White", "Black", "Grey", "Cyan", " Purple", "Brown"]
    antal =  Products.query.count()
    while antal < 500:
        products = Products()
        products.Name = "Products" + str(antal)
        products.Price = random.uniform(30.49,999.99)
        products.Color = random.choice(color)
        db.session.add(products)
        db.session.commit()
        antal = antal + 1