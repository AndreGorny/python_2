import requests

response = requests.get(url="http://ptsv2.com")

print(response.status_code)

# print(type(response))
