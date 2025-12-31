import requests
data=requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
data=data.json()

print(data["text"])
