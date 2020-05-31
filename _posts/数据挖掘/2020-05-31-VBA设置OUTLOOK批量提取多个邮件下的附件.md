---
layout: post
title: VBA设置OUTLOOK批量提取多个邮件下的附件
date: '2020-05-31 23:12:00 +0800'
categories: VBA
---

>设置Outlook收件箱（Inbox）下建立子文件夹attachment；

>计算机磁盘选定路径建立目标文件夹attachment download；

>输入代码块中的代码（文件夹名和路径名）

````YMAL
Sub Savetheattachment()
         Dim olApp As New Outlook.Application
         Dim nmsName As Outlook.NameSpace
         Dim vItem As Object
         Set nmsName = olApp.GetNamespace("MAPI")
         Set myfolder = nmsName.GetDefaultFolder(olFolderInbox)
         Set fldFolder = myfolder.Folders("attachment")
         For Each vItem In fldFolder.Items
             For Each att In vItem.Attachments
                 att.SaveAsFile "D:\attachment download\" & att.FileName
             Next
         Next
            Set fldFolder = Nothing
            Set nmsName = Nothing
End Sub
````
