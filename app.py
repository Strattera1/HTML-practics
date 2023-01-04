from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade

from model import db, seedData, Products

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Imperialguard1%40@localhost/Products'
db.app = app
db.init_app(app)
migrate = Migrate(app,db)

@app.route("/")
def startpage():
    return "<h1>Hallå<h1>"

@app.route("/kontakt")
def contactpage():
    s = "<html><head><title>Welcome</title></head><body></body></html>"
    for p in Products.query.all():
        s = s + p.Name + "<br/>"
        s = s + p.Color + "<br/>"
        s = s + str(p.Price) + "<br/>"
    s = s + "</body></html>"
    return s
    

if __name__  == "__main__":
    with app.app_context():
        upgrade()
    
        seedData(db)
        app.run()
        # while True:
        #     print("1. Create")
        #     print("2. List")        
        #     print("3. Exit")                
        #     action = input("Ange:")
        #     if action == "3":
        #         break
        #     if action == "1":
        #         print("Create")
        #     if action == "2":
        #         print("List")          