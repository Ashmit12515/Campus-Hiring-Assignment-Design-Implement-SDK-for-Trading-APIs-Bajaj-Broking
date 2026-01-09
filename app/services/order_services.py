import uuid
from app.storage.datastore import orders, trades, portfolio

def place_order(order_req):
    if order_req.quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_req.orderType == "LIMIT" and order_req.price is None:
        raise ValueError("Price required for LIMIT order")

    order_id = str(uuid.uuid4())
    executed = order_req.orderType == "MARKET"

    order = {
        "orderId": order_id,
        "symbol": order_req.symbol,
        "side": order_req.side,
        "orderType": order_req.orderType,
        "quantity": order_req.quantity,
        "price": order_req.price,
        "status": "EXECUTED" if executed else "PLACED"
    }

    orders[order_id] = order

    
    if executed:
        trade = {
            "tradeId": str(uuid.uuid4()),
            "orderId": order_id,
            "symbol": order_req.symbol,
            "quantity": order_req.quantity,
            "price": 100.0  # mocked execution price
        }
        trades.append(trade)
        holding = portfolio.get(order_req.symbol)

        if not holding:
            portfolio[order_req.symbol] = {
                "symbol": order_req.symbol,
                "quantity": order_req.quantity,
                "averagePrice": trade["price"]
            }
        else:
            total_qty = holding["quantity"] + order_req.quantity
            total_cost = (
                holding["quantity"] * holding["averagePrice"]
                + order_req.quantity * trade["price"]
            )

            holding["quantity"] = total_qty
            holding["averagePrice"] = total_cost / total_qty

    return {
        "orderId": order_id,
        "status": order["status"]
    }

        

def get_order(order_id: str):
    order = orders.get(order_id)
    if not order:
        raise ValueError("Order not found")
    return order
