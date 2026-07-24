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
dani["Did we buy?"] = np.where(dani['MEAN20'] > dani['MEAN50'], 1, 0)
dani["What to do?"] = dani["Did we buy?"].diff().fillna(0)
kupivli = dani[dani["What to do?"] != 0][["Close", "MEAN20", "MEAN50", "Did we buy?", "What to do?"]]
buys = dani[dani["What to do?"] == 1]["Close"]
sells = dani[dani["What to do?"] == -1]["Close"]
if sells.index[0] < buys.index[0]:
    sells = sells.iloc[1:]
n_trades = min(len(buys), len(sells))
pnl = ((sells.iloc[:n_trades].values - buys.iloc[:n_trades].values)/ buys.iloc[:n_trades].values) * 1000
print("Прибуток/збиток з кожної угоди ($):", pnl.round(2))
print("Загальний фінансовий результат ($):", round(pnl.sum(), 2))
