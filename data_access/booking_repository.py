from data_access.models import Booking
from sqlalchemy.orm.session import Session

class BookingRepository:
    def __init__(self, session: Session) -> None:
        self.session = session
    
    def get(self, **filters):
        pass

    def list(self):
        return self.session.query(Booking).all()

    def add(self, restaurant, date_time, party_size):
        booking = Booking(
                restaurant_id=restaurant,
                date_time=date_time,
                party_size=party_size,
            )
        self.session.add(booking)
        return booking

    def update(self, **kwargs):
        pass

    def delete(self, id_):
        pass


