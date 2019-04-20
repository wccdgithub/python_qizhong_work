import requests
from lxml import etree
import MySQLdb


link = "http://www.santostang.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
r = requests.get(link, headers=headers)


html = etree.HTML(r.text)
conn=MySQLdb.connect( host='localhost',user='root',passwd='123456',db='py',charset="utf8")
cur=conn.cursor()

title_list = html.xpath('//h1[@class="post-title"]/a/text()')
for i in title_list:
    cur.execute("insert into urls (content) values(%s)",i)
cur.close()
conn.commit()
conn.close()