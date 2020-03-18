# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:15:16 2020

@author: Administrator
"""
import xlwt
import numpy as np
x=np.arange(4000,30000,500)
y=np.arange(1000,6000,500)
# x=8000;
# y=3000;
#月工资与年终奖分开算，即年终奖不分摊到每月，年总为Z

a=b=c=1
workbook = xlwt.Workbook()  # 新建一个工作簿
sheet1 = workbook.add_sheet("适合分开纳税")  # 在工作簿中新建一个表格
sheet1.write(0, 1, "正常月工资")
sheet1.write(0, 2, "年终兑现评弹月奖金")
sheet1.write(0, 3, "最低纳税额")

sheet2 = workbook.add_sheet("适合并入每月计算")  # 在工作簿中新建一个表格
sheet2.write(0, 1, "正常月工资")
sheet2.write(0, 2, "年终兑现评弹月奖金")
sheet2.write(0, 3, "最低纳税额")

sheet3 = workbook.add_sheet("两种方法无差别")  # 在工作簿中新建一个表格
sheet3.write(0, 1, "正常月工资")
sheet3.write(0, 2, "年终兑现评弹月奖金")
sheet3.write(0, 3, "最低纳税额")

#月工资与年终奖合并计算，即年终奖分摊到每月,年总为P
for m in range(0,len(x),1):
    for n in range(0,len(y),1):
        if (x[m]-5000) <= 3000:
            X = (x[m]-5000)*0.03-0
        
        elif  (x[m]-5000) <= 12000:
            X = (x[m]-5000)*0.1-210   
        
        elif  (x[m]-5000) <= 25000:
            X = (x[m]-5000)*0.2-1410  #Z=12*X+Y  
          
            
            
        if y[n] <= 3000:
            Y = 12*y[n]*0.03-0
        
        elif  y[n] <= 12000:
            Y = 12*y[n]*0.1-210
        
        elif  y[n] <= 25000:
            Y = 12*y[n]*0.2-1410   #Z=12*X+Y
            
            
            
        if (x[m]+y[n]-5000) <= 3000:
            P = 12*((x[m]+y[n]-5000)*0.03-0)
          
        elif (x[m]+y[n]-5000) <= 12000:
            P = 12*((x[m]+y[n]-5000)*0.1-210)
          
        elif (x[m]+y[n]-5000) <= 25000:
            P = 12*((x[m]+y[n]-5000)*0.2-1410)
            
            
        if (12*X+Y-P) < 0:
            print("适合分开纳税：")
            print(x[m],y[n],12*X+Y-P)
            print("正在写入数据")
            sheet1.write(a, 1, str(x[m]))  # 表格中写入数据（对应的行和列）
            sheet1.write(a, 2, str(y[n]))  
            sheet1.write(a, 3, str(12*X+Y))  
            workbook.save("C:\\Users\\Administrator\\Desktop\\个人所得税计算3.xls")  # 保存工作簿
            a=a+1
            
        elif (12*X+Y-P) > 0:
            print("适合并入每月计算：")
            print(x[m],y[n],12*X+Y-P)
            print("正在写入数据")
            sheet2.write(b, 1,str(x[m]))  # 表格中写入数据（对应的行和列）
            sheet2.write(b, 2,str(y[n]))  
            sheet2.write(b, 3,str(P))  
            workbook.save("C:\\Users\\Administrator\\Desktop\\个人所得税计算3.xls")  # 保存工作簿
            b=b+1
            
        elif (12*X+Y-P) == 0:
            print("两种方法无差别：")
            print(x[m],y[n],12*X+Y-P)
            print("正在写入数据")
            sheet3.write(c, 1,str(x[m]))  # 表格中写入数据（对应的行和列）
            sheet3.write(c, 2,str(y[n]))  
            sheet3.write(c, 3, str(12*X+Y))  
            c=c+1
            workbook.save("C:\\Users\\Administrator\\Desktop\\个人所得税计算3.xls")  # 保存工作簿



 
 


