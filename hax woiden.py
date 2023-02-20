import requests
from bs4 import BeautifulSoup
from lxml import etree
import time

url1 = 'https://hax.co.id/create-vps/'
url2 = 'https://woiden.id/create-vps/'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
}
def get_hax():
    response1 = requests.get(url=url1,headers=headers)
    html1 = etree.HTML(response1.text)
    divs1 = html1.xpath('/html/body/main/div/div/div[2]/div/div/div/div/div/form/div[1]')
    for div1 in divs1:
        dc1 = div1.xpath('./select/option/text()')
    return dc1
def get_woiden():
    response2 = requests.get(url=url2,headers=headers)
    html2 = etree.HTML(response2.text)
    divs2 = html2.xpath('/html/body/main/div/div/div[2]/div/div/div/div/div/form/div[1]')
    for div2 in divs2:
        dc2 = div2.xpath('./select/option/text()')
    return dc2
def bj_hax(result3,result1):
    if result3 != result1:
        result3.pop(0)
        print(result3)
    else:
        pass
def bj_woiden(result4,result2):
    if result4 != result2:
        result4.pop(0)
        print(result4)
    else:
        pass
result1 = get_hax()
result2 = get_woiden()
while True:
    time.sleep(20)
    result3 = get_hax()
    result4 = get_woiden()
    bj_hax(result3,result1)
    bj_woiden(result4,result2)
    result1 = result3.insert(0,'-select-')
    result2 = result4.insert(0,'-select-')
