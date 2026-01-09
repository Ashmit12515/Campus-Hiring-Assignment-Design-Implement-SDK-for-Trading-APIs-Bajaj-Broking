# Campus-Hiring-Assignment-Design-Implement-SDK-for-Trading-APIs-Bajaj-Broking
This project implements a simplified trading backend using RESTful APIs, simulating core workflows of an online stock broking platform. The system allows users to view instruments, place buy/sell orders, track order status, view executed trades, and fetch portfolio holdings.  No real market connectivity is used. All data is stored in memory.

# Trading REST API – Backend Assignment

## Overview
A simplified trading backend built using RESTful APIs.  
The system simulates core stock broking workflows such as placing orders, executing trades, and maintaining a portfolio using in-memory storage.

---

## Technology Stack
- Python 3.11  
- FastAPI  
- REST + JSON  
- In-memory storage  
- Swagger / OpenAPI (auto-generated)

---

## Setup & Run

```bash
python -m venv venv
venv\Scripts\activate
```
```bash    
pip install fastapi uvicorn pydantic
```
```bash
python -m uvicorn app.main:app
```
Swagger UI:
```bash
http://localhost:8000/docs
```
## API Endpoints
```bash
GET  /api/v1/instruments
POST /api/v1/orders
GET  /api/v1/orders/{orderId}
GET  /api/v1/trades
GET  /api/v1/portfolio
```
## Order Execution Logic
- Market orders execute immediately

- Limit orders are placed but not executed (simplified)

- Each executed order creates a trade

- Portfolio is derived from executed trades

## Sample Request
```bash
Copy code
curl -X POST http://localhost:8000/api/v1/orders \
-H "Content-Type: application/json" \
-d '{
  "symbol":"AAPL",
  "side":"BUY",
  "orderType":"MARKET",
  "quantity":10
}'
```
