import requests

query = input('enter something:')
url = f'https://www.sogou.com/web?query={query}'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
}
response = requests.get(url = url,headers = headers)
filename = query+'.html'
with open(filename,'w',encoding='utf-8') as wp:
    wp.write(response.text)
print('Success')