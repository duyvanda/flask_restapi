from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from flask_admin import Admin


app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data/sale.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

admin = Admin(app=app)
db = SQLAlchemy(app=app)