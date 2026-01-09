from app.storage.datastore import portfolio

def get_portfolio():
    return list(portfolio.values())
