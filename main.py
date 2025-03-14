import ccxt

with open("key/binance_key.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret_key = lines[1].strip()

exchange = ccxt.binance(
    config={"apiKey": api_key, "secret": secret_key, "enableRateLimit": True}
)

# balance
balance = exchange.fetch_balance()
usdt_balance = balance["USDT"]
print(usdt_balance["total"])


# print("sks")
