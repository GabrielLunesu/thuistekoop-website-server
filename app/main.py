from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.api.property_module.views import router as PropertyRouter
from app.api.booking_module.views import router as booking_router


api_router = APIRouter(
    prefix="/api/v1",
)

app = FastAPI(title="Thuistekoop")
app.include_router(PropertyRouter, tags=["Property"], prefix="/api/v1/property")
app.include_router(booking_router)



# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api_router.get("/test")
async def Test():
    return {"message": "Server Running Properly"}


app.include_router(api_router)

