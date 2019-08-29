---
layout: post
title : Python连接Mysql
data : '2019-08-29 21:00:00 +0800'
categories: Python
---
```YMAL
import pymysql
import pandas as pd
db = pymysql.connect(host='localhost',user='root',passwd='登录密码',db='mysql',port=3306,charset='utf8')
#cursor = db.cursor()
#data = cursor.execute('SELECT * FROM `db`')
#one = cursor.fetchone()
#print(data)
#print(one)
sql = 'SELECT * FROM `db`'
df = pd.read_sql(sql,db)
print(df)
```
