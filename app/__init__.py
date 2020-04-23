from flask import Flask
from config import Config
from app.extensions import db, migrate, login_manager
from app.base.routes import blueprint as base_blueprint


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(base_blueprint)
    register_extensions(app)
    return app
