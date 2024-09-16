from data_access import models
from schemas import business
from sqlalchemy.orm.session import Session

class BookingRepository:
    def __init__(self, session: Session) -> None:
        self.session = session
    
    def get(self, **filters):
        pass

    def list(self):
        return [booking.dict() for booking in 
                self.session.query(models.Booking).all()]

    def add(self, restaurant, date_time, party_size):
        booking = models.Booking(
                restaurant_id=restaurant,
                date_time=date_time,
                party_size=party_size,
            )
        self.session.add(booking)
        print(f'{self.session = }')
        return business.Booking(
            restaurant_id=restaurant,
            date_time=date_time,
            party_size=party_size,
            _booking_record=booking
        )

    def update(self, **kwargs):
        pass

    def delete(self, id_):
        pass


