import requests

api_token = "token"
zone_name = "name"

headers = {
    "Authorization": f"Bearer {api_token}"
}

# This is a general endpoint — specific IP list access may vary
url = f"https://api.brightdata.com/zone/ips?zone={zone_name}"

response = requests.get(url, headers=headers)
data = response.json()

print(data)