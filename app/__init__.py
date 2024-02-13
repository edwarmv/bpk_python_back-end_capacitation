from flask import Flask
from sqlalchemy import text
from config import Config

from app.extensions import db, migrate, api
from app.resources.user import UserResource


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)
    api.add_resource(UserResource, "/user", "/user/<string:uuid>")
    api.init_app(app)

    with app.app_context():
        db.session.execute(text('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";'))
        db.session.commit()

    # Register blueprints here

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    return app
