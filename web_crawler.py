import requests
from lxml import html

ans = []
url = 'http://thought.so'
link = requests.get(url)

text =  html.fromstring(link.text)

#scrape all links on page
for link in text.xpath('//a/@href'):
    if link == '#header' or link == '#footer':
        continue
    ans.append(link)

#scrape all links of imageswe 
for pic in text.xpath('//img/@src'):
    if link == '#header' or link == '#footer':
        continue
    ans.append(link)