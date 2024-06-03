import numpy as np
import pandas as pd


class CandlestickAnalysis:
    def __init__(self, df):
        self.df = df

    def calculate_smma(self, src, length):
        smma = pd.Series(index=src.index, dtype=float)

        for i in range(len(src)):
            if pd.isna(smma.iloc[i - 1]):
                smma.iloc[i] = src.iloc[:i + 1].mean()
            else:
                smma.iloc[i] = (smma.iloc[i - 1] * (length - 1) + src.iloc[i]) / length

        return smma

    def cross_smma(self):
        for i in range(len(self.df)):
            if self.df.loc[i, "close"] > self.df.loc[i, "SMMA_5"] and self.df.loc[i, "open"] < self.df.loc[i, "SMMA_5"]:
                self.df.loc[i, "cross_bull"] = 1
            else:
                self.df.loc[i, "cross_bull"] = 0

            if self.df.loc[i, "open"] > self.df.loc[i, "SMMA_5"] and self.df.loc[i, "close"] < self.df.loc[i, "SMMA_5"]:
                self.df.loc[i, "cross_bear"] = 1
            else:
                self.df.loc[i, "cross_bear"] = 0
        return self.df


