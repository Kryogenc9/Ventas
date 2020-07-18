from project import ma
from project.models import Ventas


class VentasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ventas
        load_instance = True


ventas_schema = VentasSchema()
