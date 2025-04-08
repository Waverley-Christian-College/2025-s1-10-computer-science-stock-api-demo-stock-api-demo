import requests
import matplotlib.pyplot as plt

# --- Step 1: Set your parameters ---
symbol = "AAPL"
range_ = "1mo"
interval = "1d"

# --- Step 2: Build the API URL ---
url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range={range_}&interval={interval}"

# --- Step 3: Make the request ---
response = requests.get(url)
data = response.json()

# --- Step 4: Extract and process data ---
timestamps = data['chart']['result'][0]['timestamp']
prices = data['chart']['result'][0]['indicators']['quote'][0]['close']

# Optional: Convert Unix timestamps to dates (for better x-axis labels)
from datetime import datetime
dates = [datetime.fromtimestamp(ts).strftime('%Y-%m-%d') for ts in timestamps]

# --- Step 5: Plot the graph ---
plt.figure(figsize=(10, 5))
plt.plot(dates, prices, marker='o')
plt.title(f"{symbol} Stock Price Over {range_}")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
