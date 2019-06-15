from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import urllib.request
import os

def chushi():
    firefox_options=Options()
    firefox_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0"')
    firefox_options.add_argument('-disable-gpu') 
    driver=webdriver.Firefox()
    time.sleep(3)
    driver.get("https://kyfw.12306.cn/otn/resources/login.html")
    time.sleep(3)
    """ 点击账号密码登录模块 """
    element=driver.find_element_by_xpath("/html/body/div[2]/div[2]/ul/li[2]/a")
    ac=ActionChains(driver)
    ac.move_to_element(element).click().perform()
    time.sleep(1)
    return driver
def downs():
    driver=chushi()
    """ 图片下载 """
    Img=driver.find_element_by_xpath("//*[@id='J-loginImg']")   
    img_src=Img.get_attribute("src")   
    try:
        path=savepic(img_src,"yzm")
        time.sleep(3)
    except:
        pass

    """ 上传到网站上识别 """
    try:
        clicks=postImg(path)
    except:
        pass
    """ 点击验证码图片 """
    
    time.sleep(2)
    
    for i in clicks:
        if i.isdigit():
            click_yzm(int(i)-1,driver)
        else:
            print("识别网站出现错误")
            downs()
    
    driver.find_element_by_id("J-userName").send_keys("18858710494")
    driver.find_element_by_id("J-password").send_keys("wcc7883965298")
    time.sleep(1)
    driver.find_element_by_id("J-login").click()
    time.sleep(0.5)   
    check=driver.find_element_by_class_name("lgcode-success").get_attribute("style")
    if(check!='display: block;'):
        downs()
    else:
        print("验证成功")

""" 图片下载 """
def savepic(src,file):
    _path = os.getcwd()
    new_path = os.path.join(_path , 'pictures')
    if not os.path.isdir(new_path):
        os.makedirs(new_path)
        new_path += '\\'
    else:
        new_path += '\\'
    new_path=new_path + '%s.jpg' %file 
    urllib.request.urlretrieve(src, new_path)
    return new_path


""" 图片识别 """

def postImg(path):
    firefox_options=Options()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('-disable-gpu')
    driver2=webdriver.Firefox()
    driver2.get("http://littlebigluo.qicp.net:47720/")
    time.sleep(2)

    driver2.find_element_by_name('pic_xxfile').send_keys(path)
    time.sleep(1)
    driver2.find_element_by_xpath('/html/body/form/input[2]').click()
    time.sleep(1)
    str1=driver2.find_element_by_xpath('/html/body/p[1]/font').text
    str2=str(str1).split(" ")
    return str2


""" 验证码点击 """
def click_yzm(i,driver): 
    element=driver.find_element_by_xpath("//*[@id='J-loginImg']") 
    time.sleep(1)
    if (int(i)<4):
        ActionChains(driver).move_to_element_with_offset(element,50+int(i)*66,70).click().perform()
    else:
        ActionChains(driver).move_to_element_with_offset(element,50+(int(i)-4)*66,140).click().perform()

downs()
