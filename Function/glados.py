import requests
import json
import re

cookie = "_ga=GA1.2.998417645.1605580231; koa:sess=eyJ1c2VySWQiOjU0Njk5LCJfZXhwaXJlIjoxNjMxNTAwODEwNDM1LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=gK5VhB-lPQHSX1vFA3zLyWl7UhA; __cfduid=de4914d65d0995675384ce549f60d508e1611302936; _gid=GA1.2.946516349.1611302940"
url1= "https://glados.rocks/api/user/checkin"
url2= "https://glados.rocks/api/user/status"
user1="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"
user2="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"

accept='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
referer='https://glados.rocks/console'

checkin = requests.post(url1,headers={
    'authority': 'glados.rocks',
    'method': 'POST',
    'path': '/api/user/checkin',
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-length': '26',
    'content-type':'application/json;charset=UTF-8',
    'cookie': cookie,
    'origin': 'https://glados.rocks',
    'referer': 'https://glados.rocks/console/checkin',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user1},data=json.dumps({'token': "glados_network"}))
state = requests.get(url2,headers={'accept':accept,'referer': referer,'user-agent':user2,'cookie': cookie})
print(re.findall(r"\"message\":\"[^\"]*\"",checkin.text))
print(re.findall(r"\"leftDays\":\"[^\"]*\"",state.text))
checkdetail=re.findall(":checkin:[\d-]*",checkin.text)
for i in checkdetail:
    print(i[1:])