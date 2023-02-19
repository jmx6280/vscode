import requests
import re
import csv

url = 'https://movie.douban.com/chart'
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36'
}
page = requests.get(url=url,headers=headers).text
obj = re.compile(r'<table width="100%" class="">.*?<div class="pl2">.*?class="">(?P<name>.*?)/ <span style="font-size:13px;">.*?<p class="pl">(?P<year>\d{4}).*?'
                 r'<span class="rating_nums">(?P<score>.*?)</span>.*?<span class="pl">(?P<number>.*?)</span>',re.S)
result = obj.finditer(page)
file = open('data.csv','w',encoding='utf-8',newline='')
csvwriter = csv.writer(file)
for it in result:
    #print(it.group('name'))
    #print(it.group('score'))
    #print(it.group('number'))
    #print(it.group('year'))
    dic = it.groupdict()
    dic['name'] = dic['name'].strip()
    dic['score'] = dic['score'].strip()
    dic['number'] = dic['number'].strip()
    dic['number'] = dic['number'].strip()
    csvwriter.writerow(dic.values())
file.close()