import requests
import time
from bs4 import BeautifulSoup
from lxml import etree

url = 'https://free.vps.vc/create-vps'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    'cookie':'PHPSESSID=pr9rrhcdm33efqvgmumlggqj1c'
}
def get_vc():
    response =requests.get(url=url,headers=headers)
    html = etree.HTML(response.text)
    divs = html.xpath('/html/body/main/div[1]/div/div[4]/div/div/div/div/div/form/div[1]')
    for div in divs:
        dc = div.xpath('./select/option/text()')
        dc.pop(0)
    return dc
def bj_vc(result2,result1):
    if result2 != result1:
        print(result2)
    else:
        pass
result1 = get_vc()
while True:
    time.sleep(20)
    result2 = get_vc()
    bj_vc(result2,result1)
    result1 = result2
