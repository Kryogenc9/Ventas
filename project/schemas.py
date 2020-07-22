from project import ma
from project.models import Ventas, Venta_producto


'''class ProductoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Producto
        load_instance = True'''


class VentasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ventas
        load_instance = True


class Venta_productoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Venta_producto
        load_instance = True


ventas_schema = VentasSchema()

Venta_producto_schema = Venta_productoSchema()
