import requests

api_url= "https://api.mockytonk.com/proxy/ab2198a3-cafd-49d5-8ace-baac64e72222"
response = requests.get(api_url)
print(response.json())
print(response.status_code)