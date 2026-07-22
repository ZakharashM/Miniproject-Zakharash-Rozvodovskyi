import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

dani = yf.download("AAPL", start="2024-06-01", end="2026-01-01")
if isinstance(dani.columns, pd.MultiIndex):
    dani.columns = dani.columns.get_level_values(0)
dani.dropna(inplace=True)
dani = dani[['Open', 'High', 'Low', 'Close', 'Volume']]
dani["MEAN20"] = dani["Close"].rolling(20).mean()
dani["MEAN50"] = dani["Close"].rolling(50).mean()
dani = dani.loc["2025-01-01":]
print(dani)
