---
layout : post
title : Python调取百度地图API生成热力图
data : '2019-08-29 21:21:00 +0800'
categories: Python
---
`1.由中文位置生成json格式的经纬度数据`

`2.将步骤1的经纬度数据复制到百度API示例中的热力地图代码中即可生成热力图`

>pyecharts包可替代
<!-- more -->

```YMAL
import json
from urllib.request import urlopen, quote
import re

##由中文位置转换为json格式的经纬度
url = 'http://api.map.baidu.com/geocoding/v3/'
output = 'json'
ak = '密钥'#http://lbsyun.baidu.com/
add = quote("昆明市") #由于本文城市变量为中文，为防止乱码，先用quote进行编码
uri = url + '?' + 'address=' + add + '&output=' + output +'&ak=' + ak + '&callback=showLocation'##服务文档http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding
print(uri)##生成API转换链接
req = urlopen(uri)
res = req.read().decode()#将其他编码的字符串解码成unicode
print(type(res))
rey = re.findall(r'[(](.*?)[)]', res) ##提取字符串（）内的json元素
print(rey[0])##形成json格式元素
temp = json.loads(rey[0])##解析
print(temp)

lng = temp['result']['location']['lng'] ##提取经度
lat = temp['result']['location']['lat']##提取纬度
str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) +'},'##缺少权重数据，需要另加
print(str_temp) 
##之后把数据copy到百度热力地图api ‘http://lbsyun.baidu.com/jsdemo.htm#c1_15’，以权重数值为热力深度即可形成热力图
```
