---
layout : post
title : Python爬取猫眼网电影评论数据
data : '2019-08-29 21:16:00 +0800'
categories: Python
---
`以爬取猫眼网电影《邪不胜正》观众评论数据为例`

`爬取70页5万余条评论`
<!-- more -->
```YMAL
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:23:47 2019

@author: Administrator
"""

import requests

import json

import time

import random



#下载第一页数据
# %% cell 1
def get_one_page(url):

	headers = {

		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'

	}

	response = requests.get(url,headers=headers)

	if response.status_code == 200:

		return response.text

	return None



#解析第一页数据

def parse_one_page(html):

	data = json.loads(html)['cmts']

	for item in data:

		yield{

		'comment':item['content'],

		'date':item['time'].split(' ')[0],

		'rate':item['score'],

		'city':item['cityName'],

		'nickname':item['nickName']

		}



#保存数据到文本文档

def save_to_txt():

	for i in range(1,70):

		url = 'http://m.maoyan.com/mmdb/comments/movie/248566.json?_v_=yes&offset=' + str(i)

		html = get_one_page(url)

		print('正在保存第%d页。'% i)

		for item in parse_one_page(html):

			with open('xie_zheng.txt','a',encoding='utf-8') as f:

				f.write(item['date'] + ',' + item['nickname'] + ',' + item['city'] + ',' +str(item['rate'])+','+item['comment']+'\n')

		time.sleep(5 + float(random.randint(1, 100)) / 20)



if __name__ == '__main__':

	save_to_txt()
# %% cell2   
def xie_zheng(infile,outfile):

	infopen = open(infile,'r',encoding='utf-8')

	outopen = open(outfile,'w',encoding='utf-8')

	lines = infopen.readlines()

	list_l = []

	for line in lines:

		if line not in list_l:

			list_l.append(line)

			outopen.write(line)

	infopen.close()

	outopen.close()



if __name__ == '__main__':

	xie_zheng('xie_zheng.txt','xie_zheng3.txt')
# %% cell 3
from pyecharts import Style

from pyecharts import Geo


#读取城市数据

city = []

with open('xie_zheng.txt',mode='r',encoding='utf-8') as f:

	rows = f.readlines()

	for row in rows:

		if len(row.split(',')) == 5:

			city.append(row.split(',')[2].replace('\n',''))



def all_list(arr):

	result = {}

	for i in set(arr):

		result[i] = arr.count(i)

	return result



data = []

for item in all_list(city):

	data.append((item,all_list(city)[item]))

	style = Style(

		title_color = "#fff",

		title_pos = "center",

		width = 1200,

		height = 600,

		background_color = "#404a59"

		)



geo = Geo("《邪不压正》粉丝人群地理位置","数据来源：恋习Python",**style.init_style)

attr,value= geo.cast(data)

geo.add("",attr,value,visual_range=[0,20],

	visual_text_color="#fff",symbol_size=20,

	is_visualmap=True,is_piecewise=True, 

	visual_split_number=4)
geo.show_config()
geo.render()
# %% cell 4

import jieba

import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator



comment = []

with open('xie_zheng3.txt',mode='r',encoding='utf-8') as f:

	rows = f.readlines()

	for row in rows:

		if len(row.split(',')) == 5:

			comment.append(row.split(',')[4].replace('\n',''))



comment_after_split = jieba.cut(str(comment),cut_all=False)



wl_space_split= " ".join(comment_after_split)

#导入背景图

backgroud_Image = plt.imread('1.jpg') 

stopwords = STOPWORDS.copy()

#可以加多个屏蔽词

stopwords.add("电影")

stopwords.add("一部")

stopwords.add("一个")

stopwords.add("没有")

stopwords.add("什么")

stopwords.add("有点")

stopwords.add("这部")

stopwords.add("这个")

stopwords.add("不是")

stopwords.add("真的")

stopwords.add("感觉")

stopwords.add("觉得")

stopwords.add("还是")



#设置词云参数 

#参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状 

wc = WordCloud(width=1024,height=768,background_color='white',

	mask=backgroud_Image,font_path="C:\simhei.ttf",

	stopwords=stopwords,max_font_size=400,

	random_state=50)

wc.generate_from_text(wl_space_split)

img_colors= ImageColorGenerator(backgroud_Image)

wc.recolor(color_func=img_colors)

plt.imshow(wc)

plt.axis('off')#不显示坐标轴  

plt.show()

#保存结果到本地

wc.to_file('2.jpg')
# %% cell 5

rate = []

with open('xie_zheng3.txt',mode='r',encoding='utf-8') as f:

	rows = f.readlines()

	for row in rows:

		if len(row.split(',')) == 5:

			rate.append(row.split(',')[3].replace('\n',''))



print(rate.count('5')+rate.count('4.5'))

print(rate.count('4')+rate.count('3.5'))

print(rate.count('3')+rate.count('2.5'))

print(rate.count('2')+rate.count('1.5'))

print(rate.count('1')+rate.count('0.5'))


#饼状图


attr = ["五星", "四星", "三星", "二星", "一星"]


#分别代表各星级评论数

v1 = [3324,1788,1293,553,1653]

pie = Pie("饼图-星级玫瑰图示例", title_pos='center', width=900)

pie.add("7-17", attr, v1, center=[75, 50], is_random=True,

        radius=[30, 75], rosetype='area',

        is_legend_show=False, is_label_show=True)

pie.render()
```


