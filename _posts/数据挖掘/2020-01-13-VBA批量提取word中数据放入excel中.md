---
layout: post
title: VBA批量提取word中数据放入excel中
date: '2020-01-13 13:13:00 +0800'
categories: VBA
---

````YMAL
Sub 提取word表格()   'excel中Alt+F11调出vba窗口
    
    mypath = "C:\Users\Administrator\Desktop\1\"    '待提取的文件主目录
    myname = Dir(mypath & "*.doc")                  '待提取的文件名，此处为doc格式
    m = 1
        Do While myname <> ""
        Set mydoc = GetObject(mypath & myname)
        With mydoc
            m = m + 1
            With .Tables(1)
                Cells(m, 1) = m - 1          '序号
                Range("A1:F1") = Array("序号", "姓名", "性别", "身份证号码", "政治面貌", "出生日期")
                Cells(m, 2) = Replace(.cell(1, 2).Range.Text, "", "")                'cell(1,2)表示word中第1行第2列，整条语句表示：word中第1行第2列数据放入excel中的第m行第1列
                Cells(m, 3) = Replace(.cell(1, 4).Range.Text, "", "")
                Cells(m, 4) = Replace(.cell(1, 6).Range.Text, "", "")
                Cells(m, 5) = Replace(.cell(2, 4).Range.Text, "", "")
                Cells(m, 6) = Replace(.cell(2, 6).Range.Text, "", "")
            End With
            .Close False
        End With
        myname = Dir()
        Loop
        Set mydoc = Nothing
        MsgBox "提取完成"

End Sub
````
