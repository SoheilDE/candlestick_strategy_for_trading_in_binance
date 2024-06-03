import pandas as pd
import pandas_ta as ta
from strategy import CandlestickAnalysis


def data_processor(df):
    # Assuming you have ta-lib or pandas_ta for technical analysis indicators
    df = pd.concat([df, df.ta.cdl_pattern(name=["hammer", "invertedhammer", "engulfing"])], axis=1)
    df.ta.ha(append=True)
    df_HA = df[
        ['timestamp', 'HA_open', 'HA_high', 'HA_low', 'HA_close', 'CDL_HAMMER', 'CDL_INVERTEDHAMMER', 'CDL_ENGULFING']]
    ha_ohlc = {
        "HA_open": "open", "HA_high": "high", "HA_low": "low", "HA_close": "close"
    }
    df_HA.rename(columns=ha_ohlc, inplace=True)

    # Create an instance of CandlestickAnalysis
    analysis = CandlestickAnalysis(df_HA)
    shaved_df = df_HA
    # Apply the methods
    shaved_df['SMMA_5'] = analysis.calculate_smma(shaved_df['close'], 5)
    shaved_df = analysis.cross_smma()
    shaved_df["bull_candle_pattern"] = ((shaved_df['CDL_ENGULFING'] != 0) |
                                        (shaved_df['CDL_HAMMER'] != 0)).astype(int)

    shaved_df["bear_candle_pattern"] = ((shaved_df['CDL_ENGULFING'] != 0) |
                                        (shaved_df['CDL_INVERTEDHAMMER'] != 0)).astype(int)
    shaved_df["bull_candle_pattern"] = ((shaved_df['CDL_ENGULFING'] != 0) |
                                        (shaved_df['CDL_HAMMER'] != 0)).astype(int)

    shaved_df['bull_signal'] = ((shaved_df['bull_candle_pattern'] == 1) &
                            (shaved_df['cross_bull'] == 1)).astype(int)

    shaved_df['bear_signal'] = ((shaved_df['bear_candle_pattern'] == 1) &
                            (shaved_df['cross_bear'] == 1)).astype(int)

    return shaved_df['bull_signal'].iloc[-1], shaved_df['bear_signal'].iloc[-1]
