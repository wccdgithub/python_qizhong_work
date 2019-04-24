from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
import MySQLdb

conn =MySQLdb.connect(host='localhost',user='root',passwd='admin',db='test',charset='utf8')
cur=conn.cursor()

def weather(key,dif):
    url="http://www.weather.com.cn/weather/%s.shtml"%dif
    try:
        headers={"User-Agent":"Mozilla/5.0 (Windows;U;Windows NT 6.0 x64;en-US;rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"}
        req=urllib.request.Request(url,headers=headers)
        data=urllib.request.urlopen(req)
        data=data.read()
        dammit=UnicodeDammit(data,["utf-8","gbk"])
        data=dammit.unicode_markup
        soup=BeautifulSoup(data,"lxml")
        lis=soup.select("ul[class='t clearfix'] li")
        for li in lis:
            try:
                date=li.select('h1')[0].text
                weather=li.select('p[class="wea"]')[0].text
                temp=li.select('p[class="tem"]  span')[0].text+"/"+li.select('p[class="tem"] i')[0].text
                cur.execute("insert into testmode_weather(city,date,weather,temp) values(%s,%s,%s,%s)",(key,date,weather,temp))
            except Exception as err:
                print(err)
        

    except Exception as err:
        print(err)

def main():
    citycode={"北京":"101010100","上海":"101020100","广州":"101280101","深圳":"101280601","温州":"101210701"}
    for c in citycode:
        weather(c,citycode.get(c))       
    cur.close()
    conn.commit()
    conn.close()
    
main()