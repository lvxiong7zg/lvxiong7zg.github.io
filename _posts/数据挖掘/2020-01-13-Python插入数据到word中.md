---
layout: post
title: Python插入数据到word中
date: '2020-01-13 21:38:00 +0800'
categories: Python

---
>word文档——插入——文档部件——域——邮件合并—— MergeField--title\date\content

````YMAL
from mailmerge import MailMerge
 # 打印模板
template = "C:\\Users\\Administrator\\Desktop\\1.docx"
#1.docx文档——插入——文档部件——域——邮件合并—— MergeField--title\date\content

# 创建邮件合并文档并查看所有字段
document_1 = MailMerge(template)
print("Fields included in {}: {}".format(template,document_1.get_merge_fields()))
document_1.merge(
    title=u'得趣处，几点飞翠落红',#数据采集后替换即可
    date='January 2 , 2020 ',
    content='*******', 
) 
document_1.write('C:\\Users\\Administrator\\Desktop\\2.docx')

````
