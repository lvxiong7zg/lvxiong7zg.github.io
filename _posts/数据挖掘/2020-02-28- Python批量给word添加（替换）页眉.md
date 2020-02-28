---
layout : post
title : Python批量给word添加（替换）页眉
data : '2020-02-28 11:05:00 +0800'
categories: Python
---


````YMAL 
import win32com,os,sys,re 
from win32com.client import Dispatch, constants
 
# 打开新的文件 
suoyou = os.listdir('C:\\Users\\Administrator\\Desktop\\待添加')
#print suoyou
for i in suoyou:
  wenjian_name = os.path.join('C:\\Users\\Administrator\\Desktop\\待添加',i)
  #print wenjian_name
  if os.path.isfile(wenjian_name):  
    w = win32com.client.Dispatch('Word.Application') 
    w.Visible = 0
    w.DisplayAlerts = 0
    tianjia = 'C:\\Users\\Administrator\\Desktop\\待添加\\%s' % i #准备替换的文件夹
    wancheng = 'C:\\Users\\Administrator\\Desktop\\已完成\\%s' % i #替换完成后输出的目录
    doc = w.Documents.Open('C:\\Users\\Administrator\\Desktop\\标准模版.doc') 
    w.ActiveDocument.Sections[0].Headers[0].Range.Copy()
    wc = win32com.client.constants 
    doc.Close()
 
    doc2= w.Documents.Open(tianjia) 
    w.ActiveDocument.Sections[0].Headers[0].Range.Paste()
    w.ActiveDocument.SaveAs(wancheng)
    doc2.Close()
 
    doc3 = w.Documents.Open( 'C:\\Users\\Administrator\\Desktop\\标准模版.doc') 
    w.ActiveDocument.Sections[0].Footers[0].Range.Copy()
    doc3.Close()
 
    doc4= w.Documents.Open(tianjia) 
    w.ActiveDocument.Sections[0].Footers[0].Range.Paste()
    doc4.Close()
    try:
      w.Documents.Close()
      w.Quit()
    except:
      print("添加成功")
````
