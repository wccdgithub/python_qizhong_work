
import urllib.request
import os


_path = os.getcwd()
new_path = os.path.join(_path+"/HelloWorld/HelloWorld/static" , 'pictures')
if not os.path.isdir(new_path):
    os.makedirs(new_path)
    new_path += '//'
else:
        new_path += '//'
urllib.request.urlretrieve("https://img14.360buyimg.com/n7/jfs/t21031/333/1074142291/182698/4f98542c/5b1fab6dNbca54abf.jpg", new_path + '0-1.jpg' ) 
