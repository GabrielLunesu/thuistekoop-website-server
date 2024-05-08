from fastapi import APIRouter, Body, Depends
from app.api.booking_module.db_models import Booking
from app.api.booking_module.service import create_booking, list_bookings

router = APIRouter()

@router.post("/bookings/", response_model=Booking)
async def add_booking(booking: Booking = Body(...)):
    return await create_booking(booking)

@router.get("/bookings/")
async def get_all_bookings():
    return await list_bookings()
