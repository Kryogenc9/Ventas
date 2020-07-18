from flask import request, jsonify, Blueprint
from project import db
from project.models import Ventas
from project.schemas import ventas_schema

blueprint = Blueprint('Ventas', __name__)


@blueprint.route('/Ventas', methods=['GET'])
def list():
    venta = Ventas.query.all()

    return jsonify(ventas_schema.dump(venta, many=True)), 200


@blueprint.route('/Ventas', methods=['POST'])
def create():
    venta = ventas_schema.load(request.json)

    db.session.add(venta)
    db.session.commit()

    return ventas_schema.dump(venta), 201
