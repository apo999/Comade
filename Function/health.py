import requests
import re

cookie="_ga=GA1.3.1720262211.1602687713; eai-sess=6serm2rujdf07bg3n8iftc0ba4; UUkey=916d7bd103a4f2fdbfa761e07ef09ca8; Hm_lvt_48b682d4885d22a90111e46b972e3268=1603201784,1603252182,1603407288; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1603407288"
#loclist=["120.08654","30.30897"]#school
loclist=["107.45307","31.214935"]#home
user="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43"

referer = 'https://healthreport.zju.edu.cn/'
locturnurl="https://restapi.amap.com/v3/geocode/regeo?key=729923f88542d91590470f613adb27b5&s=rsv3&language=zh_cn&location="+"%.6f,%.6f"%(float(loclist[0]),float(loclist[1]))+"&extensions=base&callback=jsonp_130471_&platform=JS&logversion=2.0&appname=https%3A%2F%2Fhealthreport.zju.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex&csid=21743429-BD54-4A16-8514-A09CAE606190&sdkversion=1.4.15"
locturned = requests.get(locturnurl,headers={'referer': referer})
loctext=locturned.text.split("\"")
submiturl='https://healthreport.zju.edu.cn/ncov/wap/default/save'
data={
    'sfymqjczrj': '0','zjdfgj': '0',
    'sfyrjjh': '0','cfgj': '0','tjgj': '0','nrjrq': '0','rjka': '0','jnmddsheng': '0',
    'jnmddshi': '0','jnmddqu': '0','jnmddxiangxi': '0','rjjtfs': '0','rjjtfs1': '0',
    'rjjtgjbc': '0','jnjtfs': '0','jnjtfs1': '0','jnjtgjbc': '0','sfqrxxss': '1',
    'sfqtyyqjwdg': '0','sffrqjwdg': '0','sfhsjc': '1','tw': '0','sfcxtz': '0',
    'sfjcbh': '0','sfcxzysx': '0','qksm': '0','sfyyjc': '0','jcjgqr': '0',
    'remark': '0','address': loctext[loctext.index("formatted_address")+2],
    'geo_api_info': '{"type":"complete","info":"SUCCESS","status":1,"ZDa":"jsonp_450605_","position":{"Q":'+loclist[1]+',"R":'+loclist[0]+',"lng":'+loclist[0]+',"lat":'+loclist[1]+'},"message":"Get ipLocation success.Get address success.","location_type":"ip","accuracy":null,"isConverted":true,"addressComponent":{"citycode":"'+loctext[loctext.index("citycode")+2]+'","adcode":"'+loctext[loctext.index("adcode")+2]+'","businessAreas":[],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"'+loctext[loctext.index("street")+2]+'","streetNumber":"'+loctext[loctext.index("streetNumber")+2]+'","country":"'+loctext[loctext.index("country")+2]+'","province":"'+loctext[loctext.index("province")+2]+'","city":"'+loctext[loctext.index("city")+2]+'","district":"'+loctext[loctext.index("district")+2]+'","township":"'+loctext[loctext.index("township")+2]+'"},"formattedAddress":"'+loctext[loctext.index("formatted_address")+2]+'","roads":[],"crosses":[],"pois":[]}',
    'area': loctext[loctext.index("province")+2]+" "+loctext[loctext.index("city")+2]+" "+loctext[loctext.index("district")+2],
    'province': loctext[loctext.index("province")+2],'city': loctext[loctext.index("city")+2],'sfzx': '0','sfjcwhry': '0','sfjchbry': '0',
    'sfcyglq': '0','gllx': '0','glksrq': '0','jcbhlx': '0','jcbhrq': '0',
    'ismoved': '0','bztcyy': '0','sftjhb': '0','sftjwh': '0','sfjcqz': '0',
    'jcqzrq': '0','jrsfqzys': '0','jrsfqzfy': '0','sfyqjzgc': '0','sfsqhzjkk': '1',
    'sqhzjkkys': '1','gwszgzcs': '0','szgj': '0','szgjcs': '0','fxyy': '0','jcjg': '0'
}
#print(loctext[loctext.index("formatted_address")+2])
locget = requests.post(submiturl,data=data,headers={'user':user,'cookie':cookie})
print(re.findall(r"\"m\":\"[^\"]*\"",locget.text)[0])

cookie="eai-sess=s4ng1njate3ptkfh6bkmsrc115; UUkey=b8f8156f7a65b37aa795cf4f7d61e9e0; _csrf=S8mwplVi9KWoF2WQ0TlCeFkhpR4lX1aJpoKgE2bhNX0%3D; _pv0=XRJlKUFMl2way3Zh6ZasvwUpdKno8L2FgghT2TAzUhzArWjlkn2N4xGmspk1JczgQzmxKOKFsVWJEmzcSHl%2FOX8BHYKiN6juLfyBPudRLkdQ4FlhUVivCfITkqg6YeD0iy6KMxI4RYKvloELvXgAVOabthpHYDwI2YtK0IinOJ%2FpIM%2BDBL3d51ziVVbfpM8vSbVXPbS9IfVOlOcXlQaNRfATVJWJTJx0hpMPny1wD9GJYG7tx1bhFSwjndKzfIE0Xib8vD9zt2JB52t8VfOOdyNGJOHFDIrhXXu%2Fi5Tyr2Lve7I6J2c%2Fynaw8T%2BBK3WBFePoFBqaJgYv1QX%2FhhccJL5ae4O2aqHz76C9DL71xUi0aQM8aYtC2E4spd%2BDr6F0KvHFet%2FOhkEKLRbjNU1ggUmO3mKO5M1LVNA7eDuaIvU%3D; _pf0=0xYOwppE7LKdiKaI8y69n1HYMYAAfdlvDe3GQKv5%2FsI%3D; _pc0=cjkYca4h2r1qV4GDJr2gv5di5ZCuHwCrqraB38kofv88QqqFw0cqLUPUdBj1tPPa; iPlanetDirectoryPro=0UC4LcbQU97EayPsiO%2B4Y9o50qkNPifkka2yyn83Cfl6BeN6KTOj%2BKWusRAqhgm9NBjF%2By0ISGuTEm22BYuHBijGLYj01A0CUlguRWffRXaAWggHn5iwMcYTLbtIi03XSDX98fjuv8YVPVh65PBOIVP3WdhKpQNtpD5k3BHaUdR%2FItJf5TLxDmAvbTUWsCA%2F%2BJUCpa%2Bp6Q4Dglj6%2FQuyQdcjcqXrO2N1ifNGB4NHp4MXfiWDD5Q9iXirc1s2qtmWARzxSWvCchA%2F9uHhiy4%2FkX1dUpjqoQckQYo2Zf8myRIBrBs%2FoZsY%2FAV7oI571rKSdc6iUxt8c1A3Bpc26ZMYsgdhWDiS9LmEGtlCCJiv%2Byo%3D; Hm_lvt_48b682d4885d22a90111e46b972e3268=1613312088; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1613312125"
loclist=["120.9806","28.0722"]#she
locturnurl="https://restapi.amap.com/v3/geocode/regeo?key=729923f88542d91590470f613adb27b5&s=rsv3&language=zh_cn&location="+"%.6f,%.6f"%(float(loclist[0]),float(loclist[1]))+"&extensions=base&callback=jsonp_130471_&platform=JS&logversion=2.0&appname=https%3A%2F%2Fhealthreport.zju.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex&csid=21743429-BD54-4A16-8514-A09CAE606190&sdkversion=1.4.15"
locturned = requests.get(locturnurl,headers={'referer': referer})
loctext=locturned.text.split("\"")
data={
    'sfymqjczrj': '0','zjdfgj': '0',
    'sfyrjjh': '0','cfgj': '0','tjgj': '0','nrjrq': '0','rjka': '0','jnmddsheng': '0',
    'jnmddshi': '0','jnmddqu': '0','jnmddxiangxi': '0','rjjtfs': '0','rjjtfs1': '0',
    'rjjtgjbc': '0','jnjtfs': '0','jnjtfs1': '0','jnjtgjbc': '0','sfqrxxss': '1',
    'sfqtyyqjwdg': '0','sffrqjwdg': '0','sfhsjc': '1','tw': '0','sfcxtz': '0',
    'sfjcbh': '0','sfcxzysx': '0','qksm': '0','sfyyjc': '0','jcjgqr': '0',
    'remark': '0','address': loctext[loctext.index("formatted_address")+2],
    'geo_api_info': '{"type":"complete","info":"SUCCESS","status":1,"ZDa":"jsonp_450605_","position":{"Q":'+loclist[1]+',"R":'+loclist[0]+',"lng":'+loclist[0]+',"lat":'+loclist[1]+'},"message":"Get ipLocation success.Get address success.","location_type":"ip","accuracy":null,"isConverted":true,"addressComponent":{"citycode":"'+loctext[loctext.index("citycode")+2]+'","adcode":"'+loctext[loctext.index("adcode")+2]+'","businessAreas":[],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"'+loctext[loctext.index("street")+2]+'","streetNumber":"'+loctext[loctext.index("streetNumber")+2]+'","country":"'+loctext[loctext.index("country")+2]+'","province":"'+loctext[loctext.index("province")+2]+'","city":"'+loctext[loctext.index("city")+2]+'","district":"'+loctext[loctext.index("district")+2]+'","township":"'+loctext[loctext.index("township")+2]+'"},"formattedAddress":"'+loctext[loctext.index("formatted_address")+2]+'","roads":[],"crosses":[],"pois":[]}',
    'area': loctext[loctext.index("province")+2]+" "+loctext[loctext.index("city")+2]+" "+loctext[loctext.index("district")+2],
    'province': loctext[loctext.index("province")+2],'city': loctext[loctext.index("city")+2],'sfzx': '0','sfjcwhry': '0','sfjchbry': '0',
    'sfcyglq': '0','gllx': '0','glksrq': '0','jcbhlx': '0','jcbhrq': '0',
    'ismoved': '0','bztcyy': '0','sftjhb': '0','sftjwh': '0','sfjcqz': '0',
    'jcqzrq': '0','jrsfqzys': '0','jrsfqzfy': '0','sfyqjzgc': '0','sfsqhzjkk': '1',
    'sqhzjkkys': '1','gwszgzcs': '0','szgj': '0','szgjcs': '0','fxyy': '0','jcjg': '0'
}
locget = requests.post(submiturl,data=data,headers={'user':user,'cookie':cookie})
print(re.findall(r"\"m\":\"[^\"]*\"",locget.text)[0])