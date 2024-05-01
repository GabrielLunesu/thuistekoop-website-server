import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"
# MONGO_DETAILS = "mongodb+srv://admin:JZ0URF8Dugb03X0C@cluster0.5m1v9fn.mongodb.net/"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.property

property_collection = database.get_collection("property_collection")


def property_helper(property_doc) -> dict:
    """
    Transform a MongoDB document to a dictionary that is more suitable for client responses.

    :param property_doc: A document from MongoDB containing property data.
    :return: A simplified dictionary of property data.
    """
    return {
        "id": str(property_doc["_id"]),
        "title": property_doc["title"],
        "address": property_doc["address"],
        "price": property_doc["price"],
        "images": property_doc["images"],
        "details": property_doc["details"],
        "description": property_doc["description"],
        "space": property_doc["space"],
        "build": property_doc["build"],
        "layoutDetailsData": property_doc["layoutDetailsData"],
        "outdoor": property_doc["outdoor"],
        "energyData": property_doc["energyData"],
        "parkdetails": property_doc["parkdetails"],
        "garagedetails": property_doc["garagedetails"],
        "biddingData": {
            "initialPrice": property_doc["biddingData"]["initialPrice"],
            "hoursUntilClose": property_doc["biddingData"]["hoursUntilClose"],
            "bids": [
                {
                    "bidder": bid["bidder"],
                    "amount": bid["amount"],
                    "time": bid["time"]
                } for bid in property_doc["biddingData"]["bids"]
            ]
        }
    }