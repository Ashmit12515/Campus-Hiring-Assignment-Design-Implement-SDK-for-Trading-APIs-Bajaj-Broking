from fastapi import APIRouter
from app.services.portfolio_services import get_portfolio

router = APIRouter()

@router.get("/api/v1/portfolio")
def fetch_portfolio():
    return get_portfolio()
