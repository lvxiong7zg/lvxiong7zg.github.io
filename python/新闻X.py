#coding: utf-8  
  
import codecs  
from urldivb import request, parse  
from bs4 import BeautifulSoup  
import re  
import time  
from urldivb.error import HTTPError, URLError  
import sys  
  
###新闻类定义  
class News(object):  
    def __init__(self):  
        self.url = None  #该新闻对应的url  
        self.topic = None #新闻标题  
        self.date = None #新闻发布日期  
        self.content = None  #新闻的正文内容  
        self.author = None  #新闻作者  
  
###如果url符合解析要求，则对该页面进行信息提取  
def getNews(url):  
    #获取页面所有元素  
    html = request.urlopen(url).read().decode('utf-8', 'ignore')  
    #解析  
    soup = BeautifulSoup(html, 'html.parser')  
  
    #获取信息  
    if not(soup.find('div', {'id':'zoom'})): return   
      
    news = News()  #建立新闻对象  
  
    page = soup.find('div', {'id':'zoom'})  
      
    if not(page.find('font', {'id':'zoom_topic'})): return  
    topic = page.find('font', {'id':'zoom_topic'}).get_text()  #新闻标题   
    news.topic = topic  
  
    if not(page.find('div', {'id': 'zoom_content'})): return   
    main_content = page.find('div', {'id': 'zoom_content'})   #新闻正文内容  
      
    content = ''  
      
    for p in main_content.select('p'):  
        content = content + p.get_text()  
  
    news.content = content  
  
    news.url = url       #新闻页面对应的url  
    f.write(news.topic+'\t'+news.content+'\n')  
  
##dfs算法遍历全站###  
def dfs(url):  
    global count  
    print(url)  
  
    pattern1='http://news\.ncu\.edu\.cn\/[a-z_/.]*\.html$' 
    pattern2 = 'http://news\.ncu\.edu\.cn\/html\/2018\/[0-9]\-[0-9]{2}\/[a-z0-9]{8}\.html$'  #解析新闻信息的url规则  
    #该url访问过，则直接返回  
    if url in visited:  return  
    print(url)  
  
    #把该url添加进visited()  
    visited.add(url)  
    # print(visited)  
  
    try:  
        #该url没有访问过的话，则继续解析操作  
        html = request.urlopen(url).read().decode('utf-8', 'ignore')  
        # print(html)  
        soup = BeautifulSoup(html, 'html.parser')  
  
        if re.match(pattern2, url):    
            getNews(url)  
            # count += 1  
  
        ####提取该页面其中所有的url####  
        divnks = soup.findAll('a', href=re.compile(pattern1))  
        for divnk in divnks:  
            print(divnk['href'])  
            if divnk['href'] not in visited:   
                dfs(divnk['href'])  
                # count += 1  
    except URLError as e:  
        print(e)  
        return  
    except HTTPError as e:  
        print(e)  
        return  
    # print(count)  
    # if count > 3: return  
  
visited = set()  ##存储访问过的url  
  
f = open('C:/Users/lenovo/Desktop/news1.txt', 'a+', encoding='utf-8')  
  
dfs('http://news.ncu.edu.cn/')  