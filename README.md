# Binance Trading Bot

**Description**  
This project is a simple trading bot that interacts with the Binance cryptocurrency exchange. The bot fetches historical data, analyzes candlestick patterns, and places buy or sell orders based on the analysis.

## Project Structure
- `binance_client.py`: Contains the `BinanceTrader` class for interacting with the Binance API.
- `strategy.py`: Contains the `CandlestickAnalysis` class for analyzing candlestick patterns.
- `signaler.py`: Processes historical data and generates trading signals.
- `trade.py`: Orchestrates the trading logic using the other modules.
- `run.py`: The main script to run the trading bot.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/binance-trading-bot.git
   cd binance-trading-bot
   ```
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration
1. Replace `'your_api_key'` and `'your_api_secret'` in `run.py` with your actual Binance API key and secret.
2. Modify the `symbol`, `limit`, and `quantity` variables in `run.py` as needed.

## Usage

To start the trading bot, run the following command:
```
python run.py
```
## Code Overview
### binance_client.py
This file contains the `BinanceTrader` class, which handles communication with the Binance API.
- `create_binance_client()`: Creates a Binance client instance.
- `get_historical_data(symbol, limit)`: Fetches historical candlestick data for a given symbol.
- `place_buy_order(symbol, quantity)`: Places a market buy order.
- `place_sell_order(symbol, quantity)`: Places a market sell order.

### strategy.py
This file contains the `CandlestickAnalysis` class, which provides methods for analyzing candlestick patterns.
- `calculate_smma(src, length)`: Calculates the Smoothed Moving Average (SMMA).
- `cross_smma()`: Detects bullish and bearish crossovers.

### signaler.py
This file processes historical data and generates trading signals.
- `data_processor(df)`: Processes the DataFrame and returns the bullish and bearish signals.

### trade.py
This file contains the main trading logic.
- `trade_bot(api_key, api_secret, symbol, limit, quantity)`: Fetches data, processes it, and places orders based on signals.

### run.py
This is the entry point of the project. It runs the trading bot in an infinite loop, fetching data and making trading decisions every minute.

## Dependencies
- `pandas`
- `numpy`
- `binance`
- `pandas_ta`

## License
This project is licensed under the MIT License. See the LICENSE file for more details.