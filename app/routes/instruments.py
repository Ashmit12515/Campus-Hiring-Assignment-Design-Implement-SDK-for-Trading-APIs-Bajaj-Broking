from fastapi import APIRouter
from app.storage.datastore import instruments
router = APIRouter()

@router.get("/api/v1/instruments")
def get_instruments():
    return instruments
