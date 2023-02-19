import requests
from bs4 import BeautifulSoup
import time

url = 'http://www.umeituku.com/bizhitupian/weimeibizhi/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
response.encoding = 'utf-8'
page = BeautifulSoup(response.text,'html.parser')
alist = page.find('div',class_='TypeList').find_all('a')
for it in alist:
    href = it.get('href')
    child_response = requests.get(url=href,headers=headers)
    child_response.encoding = 'utf-8'
    child_page = BeautifulSoup(child_response.text,'html.parser')
    src = child_page.find('div',class_='ImageBody').find('img').get('src')
    img_response = requests.get(url=src,headers=headers)
    img_name = src.split('/')[-1]
    with open(img_name,'wb') as wp:
        wp.write(img_response.content)
    print(img_name,'done')
    time.sleep(1)