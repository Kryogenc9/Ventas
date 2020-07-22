from flask import request, jsonify, Blueprint
from project import db
from project.models import Venta_producto
from project.schemas import Venta_producto_schema

blueprint = Blueprint('venta_producto', __name__)


@blueprint.route('/Ventas/venta', methods=['POST'])
def savesell():
    venta_prod = Venta_producto_schema.load(request.json)

    db.session.add(venta_prod)

    db.session.commit()

    return Venta_producto_schema.dump(venta_prod), 200


@blueprint.route('/Ventas/<id_venta>', methods=['GET'])
def showsell():
    sell = Venta_producto.query.all()

    return jsonify(Venta_producto_schema.dump(sell))
