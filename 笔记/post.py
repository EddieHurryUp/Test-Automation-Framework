import requests

url = 'http://127.0.0.1:8787/login'

headers = {'Content-Type': 'application/xxx-www-form-urlencoded'}
data = {'username': 'testuser', 'password': 'testpass'}

response = requests.post(url, headers=headers, data=data)
print(response.text)
print(response.status_code)