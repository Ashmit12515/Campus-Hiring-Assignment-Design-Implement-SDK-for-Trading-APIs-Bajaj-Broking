from fastapi import APIRouter
from app.services.trade_services import get_all_trades

router = APIRouter()

@router.get("/api/v1/trades")
def fetch_trades():
    return get_all_trades()
