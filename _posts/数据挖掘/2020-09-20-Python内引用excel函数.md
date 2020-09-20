---
layout: post
title: Python内引用excel函数
date: '2020-09-20 11:12:00 +0800'
categories: Python
---
````YMAL

#xls转换为xlsx格式
import win32com.client as win32
fname = "C:\\Users\\Administrator\\Desktop\\测试\\医疗.xls"
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open(fname)
wb.SaveAs(fname+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
wb.Close()                               #FileFormat = 56 is for .xls extension
excel.Application.Quit()
#引用EXCEL函数
from openpyxl import load_workbook 

workbook = load_workbook("C:\\Users\\Administrator\\Desktop\\测试\\医疗.xlsx")
sheet = workbook["Sheet1"]
sheet["G1"] = "补缴" #查找后补充至该字段
for i in range(2,sheet.max_row+1): 
    # sheet[f"G{i}"] = f'=VLOOKUP(A{i},$K$1:$L$5,2,0)'
    sheet[f"G{i}"] = f'=SUMIFS(L:L,K:K,A{i})'
workbook.save(filename = "C:\\Users\\Administrator\\Desktop\\测试\\医疗VLOOKUP.xlsx")
print("取数完成")
````
