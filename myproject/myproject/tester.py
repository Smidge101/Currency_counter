import requests 
import Constants

service_key = Constants.API_KEY_SERVICE
#Making request
url = f"https://v6.exchangerate-api.com/v6/{service_key}/latest/USD"

#making request
response = requests.get(url)
data = response.json()

print(data)

