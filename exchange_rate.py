import requests
import json

def EUR_to_USD(amount):
    response = requests.get("https://api.exchangeratesapi.io/latest")
    data = response.json()
    conv = data['rates']['USD']
    return amount*conv
