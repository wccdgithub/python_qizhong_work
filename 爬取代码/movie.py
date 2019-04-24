import requests
from lxml import etree
import MySQLdb

conn =MySQLdb.connect(host='localhost',user='root',passwd='admin',db='test',charset='utf8')
cur=conn.cursor()

def get_page(start_num):
    url="https://movie.douban.com/top250?start=%s&filter="%start_num
    
    response=requests.get(url)
    tree=etree.HTML(response.text)
    
    title1=tree.xpath('//span[@class="title"][1]/text()')
    title2=tree.xpath('//div[@class="hd"]/a/@href')
    return title1,title2

def get_all_page(start,end):
    title=[]
    url=[]
    for i in range(start,end-start):
        title_list,url_list=get_page(i*25)
        title+=title_list
        url+=url_list

    return title,url
    
def qu():
    title,url=get_all_page(0,10)
    for i in range(len(title)):
        cur.execute("insert into testmode_pq(title,urls) values(%s,%s)",(title[i],url[i]))
    
    cur.close()
    conn.commit()
    conn.close()

if __name__=="__main__":
    qu()
