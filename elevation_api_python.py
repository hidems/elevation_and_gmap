import requests

url = "https://api.opentopodata.org/v1/etopo1?locations=39.747114,-104.996334"
# pyaload = {"key1":"value1", "key2":"value2"}

r = requests.get(url)

data = r.json()

print(r.text)
print(data['results'][0]['elevation'])
