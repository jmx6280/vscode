import requests
from Crypto.Cipher import AES
from base64 import b64encode
import json

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36'
}
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_2021543605",
    "threadId": "R_SO_4_2021543605"
}
e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
i = 'WaK8laAF5qUqZBhR'
def get_encSecKey():
    return '36dd7a9726b73ce32ed23cf67f4d7eb4eb99792fbe38ee33b0c1aa3fa1d1906d633173b8366529031b9ab7bf93d2b3e2bd7f3cdde2d64664dab0aa4ff179063ad286c8bfde106d22b3e084bf7fa6e8e394618afee1c25fb91b88ba8057bca2bf94b309c4cac6a5d150d7312c426cd6e2f1ea9e549eb7f71fc462197b53dbc702'

def get_params(data):
    first = enc_params(data,g)
    second = enc_params(first,i)
    return second
def to_16(data):
    pad = 16-len(data)%16
    data += chr(pad)*pad
    return data
def enc_params(data,key):
    iv ='0102030405060708'
    data = to_16(data)
    aes = AES.new(key=key.encode('utf-8'),IV=iv.encode('utf-8'),mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode('utf-8'))
    return str(b64encode(bs),'utf-8')
response = requests.post(url=url,data={
    'params':get_params(json.dumps(data)),
    'encSecKey':get_encSecKey()
},headers=headers)
print(response.text)
""" function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    } """