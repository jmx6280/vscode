import requests
import re
import csv

domain = 'https://www.dytt8.net/index2.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36'
}
response = requests.get(url=domain,headers=headers)
response.encoding = 'gb2312'
obj1 = re.compile(r'迅雷电影资源.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2 = re.compile(r"<a href='(?P<herf>.*?)'>",re.S)
obj3 = re.compile(r'◎译　　名(?P<name>.*?)<br />.*?<a target="_blank" href="(?P<target>.*?)"><strong>',re.S)
file = open('movie.csv','w',encoding = 'utf-8',newline='')
csvwriter = csv.writer(file)
result1 = obj1.finditer(response.text)
for it in result1:
    ul = it.group('ul')
    result2 = obj2.finditer(ul)
    for itt in result2:
        herf = itt.group('herf')
        child_herf = 'https://www.dytt8.net' + herf
        child_response = requests.get(url=child_herf,headers=headers)
        child_response.encoding = 'gb2312'
        result3 = obj3.finditer(child_response.text)
        for iitt in result3:
            name = iitt.group('name')
            target = iitt.group('target')
            dic = iitt.groupdict()
            csvwriter.writerow(dic.values())
            print(name,target)
file.close()