import os
from datetime import datetime
from typing import List

from fastapi import APIRouter, Request
from pydantic import BaseModel, conint
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from starlette import status

from data_access.booking_repository import BookingRepository
from data_access.models import Booking

router = APIRouter()


class BookTable(BaseModel):
    restaurant: int
    party_size: conint(ge=1)
    date_time: datetime


class BookingConfirmation(BaseModel):
    booking_id: int
    restaurant: int
    party_size: int
    date_time: datetime


class BookingsList(BaseModel):
    bookings: List[BookingConfirmation]


# session_maker = sessionmaker(bind=create_engine(os.getenv("DB_URL")))


@router.get("/bookings", response_model=BookingsList)
def get_bookings(request:Request):
    with request.app.session_maker() as session:
        repo = BookingRepository(session)
        bookings = repo.list()
        return {
            # "bookings": [booking.dict() for booking in bookings]
            'bookings': repo.list()
        }


@router.post("/bookings", status_code=status.HTTP_201_CREATED, 
             response_model=BookingConfirmation)
def book_table(booking_details: BookTable, request:Request):
    with request.app.session_maker() as session:
        print(f'{session = }')
        repo = BookingRepository(session)
        booking = repo.add(
                restaurant=booking_details.restaurant,
                date_time=booking_details.date_time,
                party_size=booking_details.party_size,
            )
        session.commit()
        # return_value =  {
        #     "booking_id": booking.id,
        #     "restaurant": booking_details.restaurant,
        #     "party_size": booking.party_size,
        #     "date_time": booking.date_time,
        # }
        # print(f'{return_value = }')
        return booking.dict()