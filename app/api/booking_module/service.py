from app.api.booking_module.db_models import Booking
from fastapi import HTTPException
from app.database.create_database import database

async def create_booking(booking_data: Booking):
    # Check if the booking already exists
    if await database["bookings"].find_one({"property_id": booking_data.property_id, "booking_date": booking_data.booking_date}):
        raise HTTPException(status_code=400, detail="Booking already exists for this date.")
    
    # Create the booking
    await database["bookings"].insert_one(booking_data.dict())
    return booking_data

async def list_bookings():
    bookings = []
    async for booking in database["bookings"].find():
        bookings.append(Booking(**booking))
    return bookings
