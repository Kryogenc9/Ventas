from project import db

'''class Producto(db.Model):
    id_producto = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre_producto = db.Column(db.Text, nullable=False)
    precio = db.Column(db.Integer, nullable=False)
'''


class Ventas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    productos = db.Column(db.Text, nullable=False)
    id_producto = db.Column(db.Integer, nullable=False)
    total_venta = db.Column(db.Integer, nullable=False)
    id_usuario = db.Column(db.Integer, nullable=False)
