from bson.objectid import ObjectId
from app.database.create_database import property_collection, property_helper
# Retrieve all propertys present in the database
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from datetime import datetime
from typing import List


async def retrieve_properties():
    propertys = []
    async for property in property_collection.find():
        propertys.append(property_helper(property))
    return propertys


# Add a new property into to the database
async def add_property(property_data: dict) -> dict:
    property = await property_collection.insert_one(property_data)
    new_property = await property_collection.find_one({"_id": property.inserted_id})
    return property_helper(new_property)


# Retrieve a property with a matching ID
async def retrieve_property(id: str) -> dict:
    property = await property_collection.find_one({"_id": ObjectId(id)})
    if property:
        return property_helper(property)


# Update a property with a matching ID
async def update_property(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    property = await property_collection.find_one({"_id": ObjectId(id)})
    if property:
        updated_property = await property_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_property:
            return True
        return False
  

# Delete a property from the database
async def delete_property(id: str):
    property = await property_collection.find_one({"_id": ObjectId(id)})
    if property:
        await property_collection.delete_one({"_id": ObjectId(id)})
        return True