from fastapi import APIRouter, Body, Response,HTTPException
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from typing import List


from app.api.property_module.db_models import PropertySchema, UpdatePropertyModel
from app.api.property_module.service import (
    add_property,
    retrieve_properties,
    update_property,
    delete_property,
    retrieve_property,
    
)
from app.api.commons.api_models import (
    GenericFilterParameters,
    OrderParameters,
    Pagination,
    PaginationParameters,
    ResponseEnvelope,
    status
)
router = APIRouter()

# # book dates!

# async def add_booking_dates(property_id: str, new_dates: List[datetime]):
#     # Assuming the existence of a function that fetches a property
#     property = await get_property_data(property_id)
#     if property is None:
#         return False
    
#     if not hasattr(property, 'bookingDates'):
#         property.bookingDates = []

#     property.bookingDates.extend(new_dates)
#     # Code to save the updated property back to the database
#     await update_property_data(property)
#     return True
# @router.post("/{id}/booking-dates/")
# async def add_dates_to_property(id: str, dates: List[datetime] = Body(...)):
#     print(f"Received dates: {dates}")  # Debugging line to check what is being received
#     if await add_booking_dates(id, dates):
#         return {"msg": "Booking dates added successfully"}
#     raise HTTPException(status_code=404, detail="Property not found")



@router.post(
    
    path = "",
    response_model=ResponseEnvelope,
    operation_id="Add Property",
    summary="Create Property ",
    status_code=status.HTTP_201_CREATED,
    
)
async def add_property_data(property: PropertySchema = Body(...)):
    property = jsonable_encoder(property)
    new_property = await add_property(property)
    return ResponseEnvelope(data=new_property)
@router.get(
    
    path = "",
    response_model=ResponseEnvelope,
    operation_id="Get Property",
    summary="Get Property ",
    status_code=status.HTTP_200_OK,
    
)
async def get_property():
    property = await retrieve_properties()
    if property:
        return ResponseEnvelope(data=property)
    return ResponseEnvelope(data="Empty list returned")
@router.get(
    
    path = "/{id}",
    response_model=ResponseEnvelope,
    operation_id="Get Single Property",
    summary="Get Property By Id",
    status_code=status.HTTP_200_OK,
    
)
async def get_property_data(id):
    property = await retrieve_property(id)
    if property:
        return ResponseEnvelope(message="property data retrieved successfully",data=property )
    return ResponseEnvelope(message="Property does not exist")
@router.put(
    
    path = "/{id}",
    response_model=ResponseEnvelope,
    operation_id="Update Existing Property",
    summary="Updated Property ",
    status_code=status.HTTP_200_OK,
    
)
async def update_property_data(id: str, req: UpdatePropertyModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_property = await update_property(id, req)
    if updated_property:
        return ResponseEnvelope(
            message="property with ID: {}  update is successful".format(id),
            data=updated_property
        )
    return ResponseEnvelope(
        
        message="There was an error updating the property data.",
    )

@router.delete(
    
    path = "/{id}",
    operation_id="Delete Property",
    summary="Delete Property ",
    
)
async def delete_property_data(id: str):
    deleted_property = await delete_property(id)
    if deleted_property:
        return ResponseEnvelope(
            data="property with ID: {} removed".format(id),
            status_code=status.HTTP_200_OK
        )
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Property Not Found")