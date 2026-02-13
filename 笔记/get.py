import requests

url = 'http://127.0.0.1:8787/products'
params = {'category': 'electronics'}
response = requests.get(url, params=params)
print(response.json())