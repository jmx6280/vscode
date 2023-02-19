import requests

url = 'https://www.pearvideo.com/video_1749829'
contid = url.split('_')[1]
urlstatus = f'https://www.pearvideo.com/videoStatus.jsp?contId={contid}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36',
    'Referer': url
}
response = requests.get(url=urlstatus,headers=headers)
dic = response.json()
srcurl = dic['videoInfo']['videos']['srcUrl']
systemtime = dic['systemTime']
realurl = srcurl.replace(systemtime,f'cont-{contid}')
filename = contid+'.mp4'
with open(filename,'wb') as wp:
    wp.write(requests.get(url=realurl,headers=headers).content)
print(filename,'done')