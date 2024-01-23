from typing import List
from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    Float,
    ForeignKey,
    ForeignKeyConstraint,
    Integer,
    SmallInteger,
    String,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import date, datetime


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    uuid: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(60))
    role: Mapped[str] = mapped_column(String(20))
    deleted: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

    flight_booking: Mapped[List["FlightBooking"]] = relationship(back_populates="user")
    room_booking: Mapped[List["RoomBooking"]] = relationship(back_populates="user")


class Flight(Base):
    __tablename__ = "flights"

    uuid: Mapped[int] = mapped_column(primary_key=True)
    airlane_name: Mapped[str] = mapped_column(String(20))
    from_location: Mapped[str] = mapped_column(String(60))
    to_location: Mapped[str] = mapped_column(String(60))
    departure_time: Mapped[datetime] = mapped_column(DateTime)
    arrival_time: Mapped[datetime] = mapped_column(DateTime)
    total_seats: Mapped[int] = mapped_column(SmallInteger)
    price: Mapped[float] = mapped_column(Float)
    canceled: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

    flight_booking: Mapped[List["FlightBooking"]] = relationship(
        back_populates="flight"
    )


class FlightBooking(Base):
    __tablename__ = "flight_booking"

    uuid: Mapped[int] = mapped_column(primary_key=True)
    number_seats: Mapped[int] = mapped_column(SmallInteger)
    canceled: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    flight_uuid: Mapped[int] = mapped_column(ForeignKey("flights.uuid"))
    user_uuid: Mapped[int] = mapped_column(ForeignKey("users.uuid"))

    flight: Mapped["Flight"] = relationship(back_populates="flight_booking")
    user: Mapped["User"] = relationship(back_populates="flight_booking")


class Hotel(Base):
    __tablename__ = "hotels"

    uuid: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    country: Mapped[str] = mapped_column(String(30))
    city: Mapped[str] = mapped_column(String(40))
    address: Mapped[str] = mapped_column(String(60))

    rooms: Mapped[List["Room"]] = relationship(back_populates="hotel")


class Room(Base):
    __tablename__ = "rooms"

    room_type: Mapped[str] = mapped_column(String(30))
    price: Mapped[float] = mapped_column(Float)
    number_guests: Mapped[int] = mapped_column(SmallInteger)
    available: Mapped[bool] = mapped_column(Boolean)
    deleted: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    hotel_uui: Mapped[int] = mapped_column(ForeignKey("hotels.uuid"))

    hotel: Mapped["Hotel"] = relationship(back_populates="rooms")
    room_booking: Mapped[List["RoomBooking"]] = relationship(back_populates="room")


class RoomBooking(Base):
    __tablename__ = "room_booking"

    uuid: Mapped[int] = mapped_column(primary_key=True)
    from_date: Mapped[date] = mapped_column(Date)
    to_date: Mapped[date] = mapped_column(Date)
    canceled: Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    user_uuid: Mapped[int] = mapped_column(ForeignKey("users.uuid"))
    room_uuid: Mapped[int] = mapped_column(ForeignKey("rooms.uuid"))

    user: Mapped["User"] = relationship(back_populates="users")
    room: Mapped["Room"] = relationship(back_populates="rooms")
