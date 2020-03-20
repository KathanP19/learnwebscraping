from bs4 import BeautifulSoup
import requests
import json
url = 'https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F'
response = requests.get(url, timeout=10)
content = BeautifulSoup(response.content, "html.parser")
tbody = content.find('tbody')
colorArr = []
for color in tbody.findAll('tr'):
    colorObj={
        "colour" : color.find('a').text
    }
    colorArr.append(colorObj)
with open('colorData.json', 'w') as outfile:
    json.dump(colorArr, outfile)