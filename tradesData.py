import requests
import pandas as pd


def get_trades(symbol, limit=None):
    url = "https://api.binance.com/api/v3/trades"
    params = {
        "symbol": symbol,
        "limit": limit,
    }
    res = requests.get(url, params=params)
    value = res.json()
    df = pd.DataFrame(value)
    return df


# timestamp = 1741914756000
# Date and time (GMT): 2025년 March 14일 Friday AM 1:12:36
# Date and time (your time zone): 2025년 3월 14일 금요일 오전 10:12:36 GMT+09:00

print(get_trades("BTCUSDT"))
