import requests

url = 'http://127.0.0.1:8000/accounts/registerUser/'

response = requests.post(url)
print(response)