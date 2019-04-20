import requests
from bs4 import BeautifulSoup
import MySQLdb

conn=MySQLdb.connect( host='localhost',user='root',passwd='123456',db='test',charset="utf8")
cur=conn.cursor()

link="https://movie.douban.com/top250"
headers={'User-Agent':'Mozilla/5.0 (Windows;U;Windows NT 6.1;en-US;rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r=requests.get(link)

soup=BeautifulSoup(r.text,"xml")
div_list =soup.find_all('div',class='hd')
for i in div_list:
    name=i.a.span.text.strip()
    
    cur.execute("insert into pq (name) values(%s)",name)
cur.close()
conn.commit()
conn.close()