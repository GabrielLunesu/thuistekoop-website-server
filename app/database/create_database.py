import motor.motor_asyncio

# MONGO_DETAILS = "mongodb://localhost:27017"
MONGO_DETAILS = "mongodb+srv://admin:JZ0URF8Dugb03X0C@cluster0.5m1v9fn.mongodb.net/"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.property

property_collection = database.get_collection("property_collection")


def property_helper(property_doc) -> dict:
    """
    Transform a MongoDB document to a dictionary that is more suitable for client responses.

    :param property_doc: A document from MongoDB containing property data.
    :return: A simplified dictionary of property data.
    """
    property_data = {
        "id": str(property_doc["_id"]),
        "title": property_doc.get("title", ""),
        "address": property_doc.get("address", ""),
        "price": property_doc.get("price", ""),
        "images": property_doc.get("images", []),
        "details": property_doc.get("details", []),
        "description": property_doc.get("description", ""),
        "space": property_doc.get("space", []),
        "build": property_doc.get("build", []),
        "layoutDetailsData": property_doc.get("layoutDetailsData", {}),
        "outdoor": property_doc.get("outdoor", []),
        "energyData": property_doc.get("energyData", {}),
        "parkdetails": property_doc.get("parkdetails", []),
        "garagedetails": property_doc.get("garagedetails", []),
        "biddingData": {
            "initialPrice": property_doc.get("biddingData", {}).get("initialPrice", 0),
            "bidEndTime": property_doc.get("biddingData", {}).get("bidEndTime"),
            "bids": [
                {
                    "bidder": bid.get("bidder", ""),
                    "amount": bid.get("amount", 0),
                    "time": bid.get("time")
                } for bid in property_doc.get("biddingData", {}).get("bids", [])
            ]
        },
    }

    # Optional: Include booking data if it exists
    if "bookingData" in property_doc:
        property_data["bookingData"] = {
            "bookingSlots": [
                {
                    "bookingDate": slot.get("bookingDate"),
                    "bookingTime": slot.get("bookingTime")
                } for slot in property_doc["bookingData"].get("bookingSlots", [])
            ]
        }

    return property_data