from project import db
from sqlalchemy.orm import relationship


'''class Producto(db.Model):
    id_producto = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre_producto = db.Column(db.Text, nullable=False)
    precio = db.Column(db.Integer, nullable=False)'''


class Ventas(db.Model):
    id_venta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.DATE, nullable=False)


class Venta_producto(db.Model):
    id_venta_pk = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Integer, nullable=False)
