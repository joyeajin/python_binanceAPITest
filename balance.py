import requests as rq
import hmac
import hashlib

URL = "https://fapi.binance.com"

with open("key/binance_key.txt") as f:
    lines = f.readlines()
    API_KEY = lines[0].strip()
    SECRET_KEY = lines[1].strip()

headers = {"X-MBX-APIKEY": API_KEY}


def get_user_data(url_sub):
    now = rq.get("https://api.binance.com/api/v3/time").json()[
        "serverTime"
    ]  # 현재 시점
    message = f"timestamp={now}"
    signature = hmac.new(
        key=SECRET_KEY.encode("utf-8"),
        msg=message.encode("utf-8"),
        digestmod=hashlib.sha256,
    ).hexdigest()
    url = f"{URL}{url_sub}?{message}&signature={signature}"
    result = rq.get(url, headers=headers)
    return result.json()


balance = get_user_data("/fapi/v2/balance")  # 내 계좌 잔고
order_log = get_user_data("/fapi/v1/allOrders")  # 내 주문 내역
account = get_user_data("/fapi/v2/account")  # 내 계좌 정보
print(balance)
