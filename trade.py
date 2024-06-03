import signaler
from binance_client import BinanceTrader


def trade_bot(api_key, api_secret, symbol, limit, quantity):

    binance = BinanceTrader(api_key, api_secret)
    df = binance.get_historical_data(symbol, limit)
    bull_signal, bear_signal = signaler.data_processor(df)
    if bull_signal == 1:
        binance.place_buy_order(symbol, quantity)
    if bear_signal == 1:
        binance.place_sell_order(symbol, quantity)
