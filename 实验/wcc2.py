import requests
from bs4 import BeautifulSoup
import MySQLdb

conn=MySQLdb.connect( host='localhost',user='root',passwd='123456',db='test',charset="utf8")
cur=conn.cursor()

cur.execute("insert into urls (url,content) values('www.baidu.com','hello')")
cur.close()
conn.commit()
conn.close()