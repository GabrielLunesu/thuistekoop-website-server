from fastapi import APIRouter, Body, Response,HTTPException
from fastapi.encoders import jsonable_encoder

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