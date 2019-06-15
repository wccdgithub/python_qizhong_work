import chardet
import requests
from bs4 import BeautifulSoup
import json


title="我们 love 你们"
with open('title2.json','w',encoding='utf-8')as f:
    json.dump([title],f,ensure_ascii=False)


def cs():
    str1="我们"
    """  2 """
    str_decode=str1.encode("utf-8")
    print(str_decode)
    print(type(str_decode))
    """ 3 """
    str_decode=str1.encode("utf-8").decode("utf-8")
    print(str_decode)
    print(type(str_decode))
    """ 4 """
    str1="我们"
    str_gbk=str1.encode("gbk")
    print(chardet.detect(str_gbk))

def cs2():

    url="http://w3school.com.cn/"
    r=requests.get(url)
    r.encoding="gb2312"
    soup=BeautifulSoup(r.text,"lxml")
    xx=soup.find('div',id='d1').h2.text
    print(xx)

   
    url="http://www.sina.com.cn/"
    r=requests.get(url)
    after_gzip=r.content
    print(chardet.detect(after_gzip))
    print(after_gzip.decode('utf-8'))


        
    result=open('aa.txt','r',encoding='GBK').read()
    print(result)

    result=open('aa2.txt','r',encoding='utf-8').read()
    print(result)
    
    
    
    title="我们"
    with open('title.txt','a+',encoding='utf-8') as f:
        f.write(title)
        f.close()

    title="我们 love 你们"
    with open('title.json','w',encoding='utf-8')as f:
        json.dump([title],f)




