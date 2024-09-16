from datetime import datetime, UTC
from pydantic import BaseModel, computed_field

from data_access import models

class Booking(BaseModel):
    restaurant: int
    party_size: int
    date_time: datetime
    _id: int | None = None
    _booking_record: models.Booking | None = None


    @computed_field
    @property
    def id(self) -> int | None:
        # return self._id or self._booking_record.id
        return self._booking_record if self._booking_record else self._id

b = Booking(
    _id=1,
    restaurant=1,
    party_size=2, 
    date_time=datetime.now(UTC)
    )

print(b.model_dump())

