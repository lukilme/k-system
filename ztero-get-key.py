import requests

URL = "http://localhost:23119/better-bibtex/json/export"

resp = requests.get(URL)
data = resp.json()

print(len(data))  # quantos itens
print(data[0])    # exemplo do primeiro item
