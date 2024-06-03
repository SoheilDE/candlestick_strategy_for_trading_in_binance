import trade
import time

if __name__ == "__main__":
    api_key = 'your_api_key'
    api_secret = 'your_api_secret'
    symbol = 'BTCUSDT'
    limit = 100
    quantity = 0.001
    while True:
        trade.trade_bot(api_key, api_secret, symbol, limit, quantity)
        time.sleep(60)