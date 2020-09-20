---
layout: post
title: python实现sumifs函数功能
date: '2020-09-20 22:12:00 +0800'
categories: Python
---

````YMAL
import pandas as pd
#医疗生育表
dfyl=pd.read_excel('C:\\Users\\Administrator\\Desktop\\测试\\医疗.xls',encoding='utf-8')
print(dfyl.head())


# 汇总表
dfhz=pd.read_excel('C:\\Users\\Administrator\\Desktop\\测试\\汇总表.xlsx',encoding='utf-8')
print(dfhz["姓名"][1])
counts=dfhz['姓名'].count()-1
for i in range(0,counts): 
      dfhz["医疗单位补缴"][i] = dfyl[(dfyl.姓名 == dfhz["姓名"][i]) & (dfyl.做账期号 == dfhz["期间"][i])].医疗单位补缴.sum()
      dfhz["医疗单位"][i] = dfyl[(dfyl.姓名 == dfhz["姓名"][i]) & (dfyl.做账期号 == dfhz["期间"][i])].医疗单位.sum()
      
print(dfhz.head())
dfhz.to_excel('C:\\Users\\Administrator\\Desktop\\测试\\汇总表.xlsx', sheet_name='汇总表',index=False)
````
