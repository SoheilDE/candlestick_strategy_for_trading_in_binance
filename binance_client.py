import pandas as pd
from binance.client import Client

class BinanceTrader:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = self.create_binance_client()
        self.interval = Client.KLINE_INTERVAL_1MINUTE

    def create_binance_client(self):
        return Client(self.api_key, self.api_secret)

    def get_historical_data(self, symbol, limit):
        try:
            klines = self.client.get_klines(symbol=symbol, interval=self.interval, limit=limit)
            df = pd.DataFrame(klines, columns=[
                'timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 
                'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'
            ])
            return df
        except Exception as e:
            print(f"Error fetching historical data: {e}")
            return None

    def place_buy_order(self, symbol, quantity):
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=Client.SIDE_BUY,
                type=Client.ORDER_TYPE_MARKET,
                quantity=quantity
            )
            return order
        except Exception as e:
            print(f"Error placing buy order: {e}")
            return None

    def place_sell_order(self, symbol, quantity):
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=Client.SIDE_SELL,
                type=Client.ORDER_TYPE_MARKET,
                quantity=quantity
            )
            return order
        except Exception as e:
            print(f"Error placing sell order: {e}")
            return None