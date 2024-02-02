from flask import Flask
from sqlalchemy import text
from config import Config
from app.extensions import db, migrate

from app.models.flight import Flight
from app.models.flight_booking import FlightBooking
from app.models.hotel import Hotel
from app.models.room import Room
from app.models.room_booking import RoomBooking
from app.models.user import User


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        engine = db.get_engine()

        with engine.connect() as conn:
            conn.execute(text('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";'))
            conn.commit()

    # Register blueprints here

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    return app
