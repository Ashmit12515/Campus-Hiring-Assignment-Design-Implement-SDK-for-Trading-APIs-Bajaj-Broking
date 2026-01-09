from fastapi import APIRouter, HTTPException
from app.models.order import OrderRequest
from app.services.order_services import place_order
from app.services.order_services import get_order
from app.storage.datastore import orders
router=APIRouter()   

@router.post("/api/v1/orders", status_code=201)
def create_order(order: OrderRequest):
    try:
        return place_order(order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/api/v1/orders/{order_id}")
def fetch_order(order_id: str):
    order_id = order_id.strip()  
    try:
        return get_order(order_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/api/v1/debug/orders")
def debug_orders():
    return orders
