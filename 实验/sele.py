from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import MySQLdb
import urllib.request
import os

conn =MySQLdb.connect(host='localhost',user='root',passwd='admin',db='test',charset='utf8')
cur=conn.cursor()
class phone:
    price=""
    mark=""
    src=""
    def __init__(self,price,mark,src):
        self.price=price
        self.mark=mark
        self.src=src
   

def chushi():

    firefox_options=Options()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('-disable-gpu')
    driver=webdriver.Firefox(firefox_options=firefox_options)
    driver.get("https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=s%27j&pvid=50162fa5907141298b94bc481eebdd22")
    
    return driver

def chuphone():
    driver=chushi()  
    time.sleep(3)    


    driver.execute_script('window.scrollBy(0,6800)', '1000')
    time.sleep(3)

    lis=driver.find_elements_by_xpath("//*[@id='J_goodsList']//li[@class='gl-item']")
    count=driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[4]/span/i").text
    
    for i in range(int(count)):
        ic=0
        next=driver.find_element_by_xpath("//*[@id='J_bottomPage']/span[1]/a[9]")
        for li in lis:
            
            try:
                price=li.find_element_by_xpath(".//div[@class='p-price']//i").text
                
            except:
                price="0"
            try:
                mark=li.find_element_by_xpath(".//div[@class='p-name p-name-type-2']//em").text
                
            except:
                mark=""
            try:
                img_src=li.find_element_by_xpath(".//div[@class='p-img']//img").get_attribute("src")
                if(img_src==None):
                    img_src=li.find_element_by_xpath(".//div[@class='p-img']//img").get_attribute("data-lazy-img")
            except:
                img_src=""
            img=str(i)+"-"+str(ic)
            """ 存数据到数据库 """
            cur.execute("insert into testmode_phone(mark,price,img_index) values(%s,%s,%s)",(mark,price,img+".jpg"))
            

            """ 存图片到文件夹 """
            if 'https' not in img_src:
                img_src="https:"+img_src
            
            try:
                savepic(img_src,img)
            except:
                
                savepic(img_src,img)

            print(img)
            ic+=1
            
            
        try:
            next.click()  
            time.sleep(3)
            driver.execute_script('window.scrollBy(0,6800)', '1000')
            time.sleep(3) 
            lis=driver.find_elements_by_xpath("//*[@id='J_goodsList']//li[@class='gl-item']")
        except:
            break

    

def savedb():
    chuphone()    
    cur.close()
    conn.commit()
    conn.close()

def savepic(src,file):
    _path = os.getcwd()
    new_path = os.path.join(_path+"/HelloWorld/HelloWorld/static" , 'pictures')
    if not os.path.isdir(new_path):
        os.makedirs(new_path)
        new_path += '//'
    else:
        new_path += '//'
    urllib.request.urlretrieve(src, new_path + '%s.jpg' %file )
    
    

savedb()
        
