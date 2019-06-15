import requests
import re
import time

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        time.sleep(3)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(mlist,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            mlist.append([price , title])
    except:
        print("")



def printGoodList(mlist):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in mlist:
        count+=1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods='书包'
    sum=2
    start_url="http://s.taobao.com/search?q="+goods
    infoList=[]
    for i in range(sum):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodList(infoList)

main()