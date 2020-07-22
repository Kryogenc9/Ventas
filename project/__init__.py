import marshmallow
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from project.configs import Config

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
bcrypt = Bcrypt()


def venta_producto_blueprints(app):
    from project.endpoints.venta_producto import blueprint as venta_prod
    from project.endpoints.status import blueprint as status

    app.register_blueprint(venta_prod)
    app.register_blueprint(status)


def venta_producto_error_handler(app):
    @app.errorhandler(marshmallow.exceptions.ValidationError)
    def validation_error_handler(e):
        return jsonify(e.messages), 400


def ventas_blueprints(app):
    from project.endpoints.ventas import blueprint as ventas
    from project.endpoints.status import blueprint as status

    app.register_blueprint(ventas)
    app.register_blueprint(status)


def ventas_error_handler(app):
    @app.errorhandler(marshmallow.exceptions.ValidationError)
    def validation_error_handler(e):
        return jsonify(e.messages), 400


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    ventas_blueprints(app)
    ventas_error_handler(app)
    venta_producto_blueprints(app)
    ventas_error_handler(app)

    return app
