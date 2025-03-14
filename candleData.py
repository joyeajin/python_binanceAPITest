import requests
import pandas as pd


def get_klines(symbol, interval, start_time=None, end_time=None, limit=None):
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "startTime": start_time,
        "endTime": end_time,
        "limit": limit,
    }
    res = requests.get(url, params=params)
    value = res.json()
    df = pd.DataFrame(value)
    return df


timestamp = 1685577600000
# 23년 6월 1일 오전 9시의 타임스탬프

print(get_klines("BTCUSDT", "1h", start_time=timestamp))
