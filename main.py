import requests
import json

# --- Bright Data Proxy Gateway Config ---
PROXY_HOST = "brd.superproxy.io"
PROXY_PORT = "port"
PROXY_USER = "user_name"
PROXY_PASS = "password"

# --- Build proxy config for requests ---
proxy_url = f"http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}"
proxies = {"http": proxy_url, "https": proxy_url}

# --- Yahoo Finance API config ---
symbol = "NVDA"
range_ = "1mo"
interval = "1d"
url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range={range_}&interval={interval}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# --- Make request through Bright Data proxy ---
try:
    print(f"🔄 Fetching stock data for {symbol} through Bright Data proxy...")
    response = requests.get(url, headers=headers, proxies=proxies, timeout=10)

    print("✅ Status Code:", response.status_code)
    print("📄 Response Preview:")
except requests.exceptions.RequestException as e:
    print(f"❌ Proxy request failed: {e}")

data = response.json()
print(json.dumps(data, indent=2))