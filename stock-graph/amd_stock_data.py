import yfinance as yf
import pandas as pd
import json
import matplotlib.pyplot as plt

amd = yf.Ticker("AMD")

with open('amd.json') as json_file:
    amd_info = json.load(json_file)
    # Print the type of data variable
    # print("Type:", type(amd_info))

# print(amd_info['industry'])
# print(amd_info['sector'])
print(amd_info['country'])

# Obtain stock data for AMD using the history function, set the period to max. Find the Volume traded on the first day (first row).
amd_hist = amd.history(period="max")
# print(amd_hist)
print(amd_hist.iloc[0, 4])



