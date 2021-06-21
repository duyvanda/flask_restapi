from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean, Enum, DateTime
from sqlalchemy.orm import relationship
from app import db

#from app import app
#from app.models import *

class Category(db.Model):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    #receipts = relationship("ReceiptDetail", backref="product", lazy=True)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    db.create_all()