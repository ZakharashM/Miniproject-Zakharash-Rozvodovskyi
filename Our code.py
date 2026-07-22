import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

dani = yf.download("AAPL", start="2025-06-30", end="2025-07-20")
if isinstance(dani.columns, pd.MultiIndex):
    dani.columns = dani.columns.get_level_values(0)
dani.dropna(inplace=True)
dani = dani[['Open', 'High', 'Low', 'Close', 'Volume']]
print(dani)