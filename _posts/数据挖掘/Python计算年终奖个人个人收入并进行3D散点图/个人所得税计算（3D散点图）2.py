# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:09:32 2020

@author: Administrator
"""
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
  
fig = plt.figure()
ax = Axes3D(fig)


import pandas as pd
#读取工作簿和工作簿中的工作表
data1_frame=pd.read_excel('C:\\Users\\Administrator\\Desktop\\个人所得税计算3.xls',sheet_name='适合分开纳税')
x1=data1_frame.iloc[1:,1]
y1=data1_frame.iloc[1:,2]
z1=data1_frame.iloc[1:,3]

data2_frame=pd.read_excel('C:\\Users\\Administrator\\Desktop\\个人所得税计算3.xls',sheet_name='两种方法无差别')
x2=data2_frame.iloc[1:,1]
y2=data2_frame.iloc[1:,2]
z2=data2_frame.iloc[1:,3]

data3_frame=pd.read_excel('C:\\Users\\Administrator\\Desktop\\个人所得税计算3.xls',sheet_name='适合并入每月计算')
x3=data3_frame.iloc[1:,1]
y3=data3_frame.iloc[1:,2]
z3=data3_frame.iloc[1:,3]


# 绘制散点图
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x1, y1, z1, c='r', label='适合分开纳税')
ax.scatter(x2, y2, z2, c='g', label='两种方法无差别')
ax.scatter(x3, y3, z3, c='b', label='适合并入每月计算')
 
 
# 添加坐标轴(顺序是Z, Y, X)
ax.set_zlabel('Z', fontdict={'size': 15, 'color': 'red'})
ax.set_ylabel('Y', fontdict={'size': 15, 'color': 'red'})
ax.set_xlabel('X', fontdict={'size': 15, 'color': 'red'})

plt.show()