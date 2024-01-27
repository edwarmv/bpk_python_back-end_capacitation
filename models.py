from typing import List
from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    Float,
    ForeignKey,
    SmallInteger,
    String,
    Uuid,
    text,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import date, datetime


class Base(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class User(Base):
    __tablename__ = "users"

    uuid: Mapped[str] = mapped_column(
        Uuid(), primary_key=True, server_default=text("uuid_generate_v4()")
    )
    full_name: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(60))
    role: Mapped[str] = mapped_column(String(20))
    deleted: Mapped[bool] = mapped_column(Boolean)

    flights_booking: Mapped[List["FlightBooking"]] = relationship(back_populates="user")
    rooms_booking: Mapped[List["RoomBooking"]] = relationship(back_populates="user")


class Flight(Base):
    __tablename__ = "flights"

    uuid: Mapped[str] = mapped_column(
        Uuid(), primary_key=True, server_default=text("uuid_generate_v4()")
    )
    airlane_name: Mapped[str] = mapped_column(String(20))
    from_location: Mapped[str] = mapped_column(String(60))
    to_location: Mapped[str] = mapped_column(String(60))
    departure_time: Mapped[datetime] = mapped_column(DateTime)
    arrival_time: Mapped[datetime] = mapped_column(DateTime)
    total_seats: Mapped[int] = mapped_column(SmallInteger)
    price: Mapped[float] = mapped_column(Float)
    canceled: Mapped[bool] = mapped_column(Boolean)

    flights_booking: Mapped[List["FlightBooking"]] = relationship(
        back_populates="flight"
    )


class FlightBooking(Base):
    __tablename__ = "flights_booking"

    uuid: Mapped[str] = mapped_column(
        Uuid(), primary_key=True, server_default=text("uuid_generate_v4()")
    )
    number_seats: Mapped[int] = mapped_column(SmallInteger)
    canceled: Mapped[bool] = mapped_column(Boolean)
    flight_uuid: Mapped[str] = mapped_column(ForeignKey("flights.uuid"))
    user_uuid: Mapped[str] = mapped_column(ForeignKey("users.uuid"))

    flight: Mapped["Flight"] = relationship(back_populates="flights_booking")
    user: Mapped["User"] = relationship(back_populates="flights_booking")


class Hotel(Base):
    __tablename__ = "hotels"

    uuid: Mapped[str] = mapped_column(
        Uuid(), primary_key=True, server_default=text("uuid_generate_v4()")
    )
    name: Mapped[str] = mapped_column(String(50))
    country: Mapped[str] = mapped_column(String(30))
    city: Mapped[str] = mapped_column(String(40))
    address: Mapped[str] = mapped_column(String(60))

    rooms: Mapped[List["Room"]] = relationship(back_populates="hotel")


class Room(Base):
    __tablename__ = "rooms"

    uuid: Mapped[str] = mapped_column(
        Uuid(), primary_key=True, server_default=text("uuid_generate_v4()")
    )
    room_type: Mapped[str] = mapped_column(String(30))
    price: Mapped[float] = mapped_column(Float)
    number_guests: Mapped[int] = mapped_column(SmallInteger)
    available: Mapped[bool] = mapped_column(Boolean)
    deleted: Mapped[bool] = mapped_column(Boolean)
    hotel_uui: Mapped[str] = mapped_column(ForeignKey("hotels.uuid"))

    hotel: Mapped["Hotel"] = relationship(back_populates="rooms")
    rooms_booking: Mapped[List["RoomBooking"]] = relationship(back_populates="room")


class RoomBooking(Base):
    __tablename__ = "rooms_booking"

    uuid: Mapped[str] = mapped_column(
        Uuid(), primary_key=True, server_default=text("uuid_generate_v4()")
    )
    from_date: Mapped[date] = mapped_column(Date)
    to_date: Mapped[date] = mapped_column(Date)
    canceled: Mapped[bool] = mapped_column(Boolean)
    user_uuid: Mapped[str] = mapped_column(ForeignKey("users.uuid"))
    room_uuid: Mapped[str] = mapped_column(ForeignKey("rooms.uuid"))

    user: Mapped["User"] = relationship(back_populates="users")
    room: Mapped["Room"] = relationship(back_populates="rooms")
