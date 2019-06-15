import threading
import requests
import re
import time

g_mutex=threading.Condition()
g_pages=[]
g_queueURL=[]
g_existURL=[]
g_writecount=0

class Crawler:
    def __init__(self,url,threadnum):
        self.url=url
        self.threadnum=threadnum
        self.threadpool=[]

    def craw(self):
        global g_queueURL
        g_queueURL.append(url)
        depth=1
        while(depth<3):
            print('Searching depth',depth,'...\n')
            self.downloadAll()
            self.updateQueueURL()
            g_pages=[]
            depth+=1

    def downloadAll(self):
        global g_queueURL
        i=0
        while i<len(g_queueURL):
            j=0
            while j<self.threadnum and i+j<len(g_queueURL):
                threadresult=self.download(g_queueURL[i+j],j)
                j+=1
            i+=j
            for thread in self.threadpool:
                thread.join(30)
            threadpool=[]
        g_queueURL=[]

    def download(self,url,tid):
        crawthread=CrawlerThread(url,tid)
        self.threadpool.append(crawthread)
        crawthread.start()

    def updateQueueURL(self):
        global g_queueURL
        global g_existURL
        newUrlList=[]
        for content in g_pages:
            newUrlList+=self.getUrl(content)
        g_queueURL=list(set(newUrlList)-set(g_existURL))

    def getUrl(self,content):
        link_list=re.findall('<a href="/([^:#=<>]*?)".*?</a>',content)
 
    
        unique_list=list(set(link_list))
        return unique_list


class CrawlerThread(threading.Thread):

    def __init__(self,url,tid):
        threading.Thread.__init__(self)
        self.url=url
        self.tid=tid

    def run(self):
        global g_mutex
        global g_writecount
        try:
            print(self.tid,"crawl",self.url)
            headers={'User-Agent':'Mozilla/5.0 (Windows;U;Windows NT 6.1;en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
            r=requests.get("https://baike.baidu.com/"+self.url,headers=headers)
            r.encoding="utf-8"
            html=r.text
            
            link_list2=re.findall('<a href="/([^:#=<>]*?)".*?</a>',html)
            unique_list2=list(set(link_list2))
            for eachone in unique_list2:
                g_writecount+=1
                content2="No."+str(g_writecount)+"\t Thread"+str(self.tid)+"\t"+self.url+' --> '+eachone+'\n'
                with open('gdyx.txt',"a+",encoding='utf-8') as f:
                    print(content2)
                    f.write(content2)
                    f.close()
        except Exception as e:
            g_mutex.acquire()
            g_existURL.append(self.url)
            g_mutex.release()
            print('Failed downloading and saving',self.url)
            print(e)
            return None
        g_mutex.acquire()
        g_pages.append(html)
        g_existURL.append(self.url)
        g_mutex.release()


if __name__ == "__main__":
    time1=time.time()
    url=""
    threadnum=3
    crawler=Crawler(url,threadnum)
    crawler.craw()        
    time2=time.time()
    print("Total time",time2-time1)
