from bs4 import BeautifulSoup
import requests
import json

onl_URL = 'https://catalog.onliner.by/sdapi/catalog.api/search/{}'
url = onl_URL.format('products')
NAME_OF_FILE_3 = 'onliner_parse'
data = requests.get(url, params={'query': 'laptop+samsung', 'page': '1'}).json()

with open('result.json', 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=True)
