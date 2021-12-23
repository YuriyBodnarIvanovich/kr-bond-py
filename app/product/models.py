from app import db
import enum
from datetime import datetime

class MyEnum(enum.Enum):
    materials = 1
    products = 2
    ware = 3
    industrial = 4
    electronics = 5


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codeOfProduct = db.Column(db.Integer)
    name = db.Column(db.String(80), nullable=False)
    typeOfProduct = db.Column(db.Enum(MyEnum), default='materials')
    is_product = db.Column(db.Boolean, default=False)
    count = db.Column(db.Integer, default=0)
    price = db.Column(db.Integer, default=0)
    description =  db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Task {self.id} {self.codeOfProduct} {self.name} {self.typeOfProduct}  {self.is_product} {self.count} {self.price} {self.description}>'