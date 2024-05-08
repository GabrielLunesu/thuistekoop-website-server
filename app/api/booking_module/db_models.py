from pydantic import BaseModel, Field
from datetime import datetime

class Booking(BaseModel):
    property_id: str = Field(..., description="ID of the property")
    user_email: str = Field(..., description="Email of the user making the booking")
    booking_date: datetime = Field(..., description="Date and time of the booking")
