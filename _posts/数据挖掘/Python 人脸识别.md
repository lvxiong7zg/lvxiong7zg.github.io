---
layout: post
title: Python 人脸识别
date: '2019-08-29 20:38:00 +0800'
categories: Python
---
Face+功能介绍： https://console.faceplusplus.com.cn/dashboard

人脸识别；人体识别

证件识别；图像识别  

Python实现代码如下：
<!-- more -->
```YMAL

import requests
import simplejson
import json
import base64

def find_face(imgpath):

    print("finding")
    
    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    
    data = {"api_key": '账号',
        "api_secret": '密钥', "image_url": imgpath, "return_landmark": 1}
    
    files = {"image_file": open(imgpath, "rb")}
    
    response = requests.post(http_url, data=data, files=files)
    
    req_con = response.content.decode('utf-8')
    
    req_dict = json.JSONDecoder().decode(req_con)
    
    this_json = simplejson.dumps(req_dict)
    
    this_json2 = simplejson.loads(this_json)
    
    faces = this_json2['faces']
    
    list0 = faces[0]
    
    rectangle = list0['face_rectangle']
    
    # print(rectangle)
    
    return rectangle

#number表示换脸的相似度
def merge_face(image_url_1,image_url_2,image_url,number):
    
    ff1 = find_face(image_url_1)
    
    ff2 = find_face(image_url_2)
 
    rectangle1 = str(str(ff1['top']) + "," + str(ff1['left']) + "," + str(ff1['width']) + "," + str(ff1['height']))
    
    rectangle2 = str(ff2['top']) + "," + str(ff2['left']) + "," + str(ff2['width']) + "," + str(ff2['height'])
 
    url_add = "https://api-cn.faceplusplus.com/imagepp/v1/mergeface"
 
    f1 = open(image_url_1, 'rb')
 
    f1_64 = base64.b64encode(f1.read())
    
    f1.close()
    
    f2 = open(image_url_2, 'rb')
    
    f2_64 = base64.b64encode(f2.read())
    
    f2.close()
 
    data = {"api_key": 'awbrGs4f7fg2VI_g46fygcfWGDftbNzD', "api_secret": 'jX4-cWsMZHBKR4wQiobcNiIvwk5jJgWN',
        "template_base64": f1_64, "template_rectangle": rectangle1,
        "merge_base64": f2_64, "merge_rectangle": rectangle2, "merge_rate": number}
 
    response = requests.post(url_add, data=data)
 
    req_con = response.content.decode('utf-8')
 
    req_dict = json.JSONDecoder().decode(req_con)
 
    result = req_dict['result']
 
    imgdata = base64.b64decode(result)
 
    
    file = open(image_url, 'wb')
 
    file.write(imgdata)
 
    file.close()

    
image1 = r"C:\Users\Administrator\Desktop\huanlian\001.jpg"##脸

image2 = r"C:\Users\Administrator\Desktop\huanlian\13.jpg"##背景

image = r"C:\Users\Administrator\Desktop\huanlian\0711.jpg"

merge_face(image2,image1,image,95)
```
