from bs4 import BeautifulSoup
import requests
import json
url = 'https://simple.wikipedia.org/wiki/Colour'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
colourArr = []
ul = content.find('ul')

for colour in ul.findAll('li'):
    colourArr.append(colour.find('a').text)

with open('colourData.json', 'w') as outfile:
    json.dump(colourArr, outfile)

print(colourArr)


    
