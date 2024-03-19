from bs4 import BeautifulSoup
import requests
import json

URL = 'https://www.ncbi.nlm.nih.gov/nuccore/?term=cancer'
# site = requests.get(URL, headers={'Accept': 'application/json'})
# json_site = json.load(site)
data = requests.get(URL)
#json_daat = data.json()

print(data.text)

