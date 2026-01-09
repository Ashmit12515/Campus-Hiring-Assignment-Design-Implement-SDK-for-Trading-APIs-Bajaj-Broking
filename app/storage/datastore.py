from app.models.instrument import Instrument

instruments = [
    Instrument(
        symbol="AAPL",
        exchange="NASDAQ",
        instrumentType="EQUITY",
        lastTradedPrice=180.5
    ),
    Instrument(
        symbol="GOOG",
        exchange="NASDAQ",
        instrumentType="EQUITY",
        lastTradedPrice=135.2
    )
]

orders = {}
trades = []
portfolio = {}

