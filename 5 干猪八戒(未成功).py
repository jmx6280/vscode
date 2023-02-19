import requests
from lxml import etree

url = 'https://heilongjiang.zbj.com/search/service/?kw=saas&r=2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
html = etree.HTML(response.text)
divs = html.xpath("/html/body/div[2]/div/div/div[3]/div/div[4]/div[4]/div[1]/div")
for div in divs:
    price = div.xpath('./div/div[3]/div[1]/span/text()')
    print(price)