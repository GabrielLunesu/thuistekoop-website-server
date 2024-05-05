from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field


# class PropertySchema(BaseModel):
#     fullname: str = Field(...)
#     email: EmailStr = Field(...)
#     course_of_study: str = Field(...)
#     year: int = Field(..., gt=0, lt=9)
#     gpa: float = Field(..., le=4.0)

#     class Config:
#         schema_extra = {
#             "example": {
#                 "fullname": "John Doe",
#                 "email": "jdoe@x.edu.ng",
#                 "course_of_study": "Water resources engineering",
#                 "year": 2,
#                 "gpa": "3.0",
#             }
#         }

class DetailItem(BaseModel):
    label: str
    value: str

class LayoutDetails(BaseModel):
    aantalKamers: int
    aantalSlaapkamers: int
    aantalBadkamers: int
    aantalWoonlagen: int
    voorzieningen: List[str]

class EnergyData(BaseModel):
    isolatie: str
    verwarming: str
    warmWater: str
    cvKetel: str
    energielabel: str

class BidData(BaseModel):
    # bid_start_time: datetime
    # bid_end_time: datetime
    bidder: str
    amount: float
    time: datetime

class BiddingData(BaseModel):
    initialPrice: float
    BidEndTime: datetime
    bids: List[BidData]

class PropertySchema(BaseModel):
    title: str
    address: str
    price: str
    images: List[str]
    details: List[DetailItem]
    description: str
    space: List[DetailItem]
    build: List[DetailItem]
    layoutDetailsData: LayoutDetails
    outdoor: List[DetailItem]
    energyData: EnergyData
    parkdetails: List[DetailItem]
    garagedetails: List[DetailItem]
    biddingData: BiddingData
    class Config:
        schema_extra = {
            "example": {
                "title": "Hendrik de Swaeffstraat 11",
                "address": "5706 MX Helmond (Akkers)",
                "price": "€ 469.000 k.k.",
                "images": [
                    "https://via.placeholder.com/600x400",
                    "https://via.placeholder.com/600x400",
                    "https://via.placeholder.com/600x400"
                ],
                "details": [
                    { "label": "Woonoppervlakte", "value": "132 m²" },
                    { "label": "Perceeloppervlakte", "value": "275 m²" },
                    { "label": "Bouwjaar", "value": "1998" },
                    { "label": "Kamers", "value": "5" }
                ],
                "description": "Deze woning wordt sinds 30 april 2024 aangeboden door Adriaan van den Heuvel Makelaars en Adviseurs...",
                "space": [
                    { "label": "Woonoppervlakte", "value": "132 m²" },
                    { "label": "Perceeloppervlakte", "value": "275 m²" },
                    { "label": "Inhoud", "value": "463 m³" }
                ],
                "build": [
                    { "label": "Type woning", "value": "Huis" },
                    { "label": "Soort woning", "value": "2-onder-1-kapwoning, Eengezinswoning" },
                    { "label": "Soort bouw", "value": "Bestaande bouw" },
                    { "label": "Bouwjaar", "value": "1998" }
                ],
                "layoutDetailsData": {
                    "aantalKamers": 5,
                    "aantalSlaapkamers": 4,
                    "aantalBadkamers": 1,
                    "aantalWoonlagen": 3,
                    "voorzieningen": ['Mechanische ventilatie', 'Douche', 'Toilet', 'Buitenzonwering', 'Dakraam', 'Wasruimte']
                },
                "outdoor": [
                    { "label": "Balkon", "value": "Niet aanwezig" },
                    { "label": "Tuin", "value": "Aanwezig (110 m², gelegen op het zuiden)" },
                    { "label": "Tuinbeschrijving", "value": "achtertuin, voortuin" }
                ],
                "energyData": {
                    "isolatie": "Dubbele beglazing, Vloerisolatie, Dakisolatie, Muurisolatie",
                    "verwarming": "CV-ketel",
                    "warmWater": "CV-ketel",
                    "cvKetel": "Vaillant (Gas, uit 2016, Eigendom)",
                    "energielabel": "B"
                },
                "parkdetails": [
                    { "label": "Aanwezig", "value": "Ja" },
                    { "label": "Soort parkeergelegenheid", "value": "Openbaar" }
                ],
                "garagedetails": [
                    { "label": "Aanwezig", "value": "Ja" },
                    { "label": "Omschrijving", "value": "Vrijstaand steen" }
                ],
                "biddingData": {
                    "initialPrice": 469000,
                    "bidEndTime": datetime(2024, 4, 26, 15, 30),
                    "bids": [
                        { "bidder": 'John Doe', "amount": 470000, "time": datetime(2024, 4, 25, 14, 0) },
                        { "bidder": 'Jane Smith', "amount": 471000, "time": datetime(2024, 4, 26, 15, 30) }
                    ]
                }
            }
        }


class UpdatePropertyModel(BaseModel):
    title: str
    address: str
    price: str
    images: List[str]
    details: List[DetailItem]
    description: str
    space: List[DetailItem]
    build: List[DetailItem]
    layoutDetailsData: LayoutDetails
    outdoor: List[DetailItem]
    energyData: EnergyData
    parkdetails: List[DetailItem]
    garagedetails: List[DetailItem]
    biddingData: BiddingData
    class Config:
        schema_extra = {
            "example": {
                "title": "Hendrik de Swaeffstraat 11",
                "address": "5706 MX Helmond (Akkers)",
                "price": "€ 469.000 k.k.",
                "images": [
                    "https://via.placeholder.com/600x400",
                    "https://via.placeholder.com/600x400",
                    "https://via.placeholder.com/600x400"
                ],
                "details": [
                    { "label": "Woonoppervlakte", "value": "132 m²" },
                    { "label": "Perceeloppervlakte", "value": "275 m²" },
                    { "label": "Bouwjaar", "value": "1998" },
                    { "label": "Kamers", "value": "5" }
                ],
                "description": "Deze woning wordt sinds 30 april 2024 aangeboden door Adriaan van den Heuvel Makelaars en Adviseurs...",
                "space": [
                    { "label": "Woonoppervlakte", "value": "132 m²" },
                    { "label": "Perceeloppervlakte", "value": "275 m²" },
                    { "label": "Inhoud", "value": "463 m³" }
                ],
                "build": [
                    { "label": "Type woning", "value": "Huis" },
                    { "label": "Soort woning", "value": "2-onder-1-kapwoning, Eengezinswoning" },
                    { "label": "Soort bouw", "value": "Bestaande bouw" },
                    { "label": "Bouwjaar", "value": "1998" }
                ],
                "layoutDetailsData": {
                    "aantalKamers": 5,
                    "aantalSlaapkamers": 4,
                    "aantalBadkamers": 1,
                    "aantalWoonlagen": 3,
                    "voorzieningen": ['Mechanische ventilatie', 'Douche', 'Toilet', 'Buitenzonwering', 'Dakraam', 'Wasruimte']
                },
                "outdoor": [
                    { "label": "Balkon", "value": "Niet aanwezig" },
                    { "label": "Tuin", "value": "Aanwezig (110 m², gelegen op het zuiden)" },
                    { "label": "Tuinbeschrijving", "value": "achtertuin, voortuin" }
                ],
                "energyData": {
                    "isolatie": "Dubbele beglazing, Vloerisolatie, Dakisolatie, Muurisolatie",
                    "verwarming": "CV-ketel",
                    "warmWater": "CV-ketel",
                    "cvKetel": "Vaillant (Gas, uit 2016, Eigendom)",
                    "energielabel": "B"
                },
                "parkdetails": [
                    { "label": "Aanwezig", "value": "Ja" },
                    { "label": "Soort parkeergelegenheid", "value": "Openbaar" }
                ],
                "garagedetails": [
                    { "label": "Aanwezig", "value": "Ja" },
                    { "label": "Omschrijving", "value": "Vrijstaand steen" }
                ],
                "biddingData": {
                    "initialPrice": 469000,
                     "bidEndTime": datetime(2024, 5, 1, 12, 0), 
                    "bids": [
                        { "bidder": 'John Doe', "amount": 470000, "time": datetime(2024, 4, 25, 14, 0) },
                        { "bidder": 'Jane Smith', "amount": 471000, "time": datetime(2024, 4, 26, 15, 30) }
                    ]
                }
            }
        }
