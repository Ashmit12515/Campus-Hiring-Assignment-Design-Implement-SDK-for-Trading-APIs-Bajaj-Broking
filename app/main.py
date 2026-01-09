from fastapi import FastAPI
from app.routes import instruments
from app.routes import orders
from app.routes import instruments, orders, trades
from app.routes import portfolios
app = FastAPI(title="Trading REST API")

app.include_router(orders.router)

app.include_router(instruments.router)

app.include_router(trades.router)


app.include_router(portfolios.router)

@app.get("/")
def root():
    return {"message": "Trading API is running"}


