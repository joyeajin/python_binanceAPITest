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


timestamp = 1741914756000
# Date and time (GMT): 2025년 March 14일 Friday AM 1:12:36
# Date and time (your time zone): 2025년 3월 14일 금요일 오전 10:12:36 GMT+09:00

print(get_klines("BTCUSDT", "1h", start_time=timestamp))

# 프린트 되는 정보 =>
# 0: Kline open time(시작시간 timestamp)
# 1: Open price(시가)
# 2: High Price(고가)
# 3: Low Price(저가)
# 4: Close Price(종가)
# 5: Volume(거래량)
# 6: Kline Close time(종료시간 timestamp)
# 7: Quote asset volume(거래대금)
# 8: Number of trades(거래횟수)
# 9: Taker buy base asset volume
# 10: Taker buy quote asset volume
# 11: Unused field, ignore.
