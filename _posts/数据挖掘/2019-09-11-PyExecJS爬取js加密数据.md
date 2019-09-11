---
published: true
---
> 函数调取过程：

>getData()——getAQIData() 和 getWeatherData() ——反混淆 ——getServerData() 加密，反混淆得出——getParam()、decodeData() 

<!-- more -->
````YMAL
import execjs
import requests
# Init environment
node = execjs.get()
 
# Params
method = 'GETCITYWEATHER'
city = '昆明'
type = 'HOUR'
start_time = '2019-09-10 00:00:00'
end_time = '2019-09-10 23:00:00'
 
# Compile javascript
file = 'encryption.js'
ctx = node.compile(open(file).read())
print(ctx)
#params = ctx.eval("getEncryptedData",)
#Get params
js = 'getEncryptedData("{0}", "{1}", "{2}", "{3}", "{4}")'.format(method, city, type, start_time, end_time)
params = ctx.eval(js)

# Get encrypted response text
api = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
response = requests.post(api, data={'d': params})

# Decode data
js = 'decodeData("{0}")'.format(response.text)
decrypted_data = ctx.eval(js)
````

>原文链接：[JavaScript加密逻辑分析与Python模拟执行实现数据爬取](https://cuiqingcai.com/5024.html "JavaScript加密逻辑分析与Python模拟执行实现数据爬取")
