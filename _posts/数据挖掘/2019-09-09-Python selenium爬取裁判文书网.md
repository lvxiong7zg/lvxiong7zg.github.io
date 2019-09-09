---
published: true
---

>采用PyQuery解析网页
>此处仅构造采取器，未打印或存储
<!-- more -->

```YMAL
from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.support.wait import WebDriverWait

#裁判文书网会不定时更新反爬机制
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
def getUrl(url):
    browser.get(url)
    html = browser.page_source
    doc = pq(html)
    items = doc('.LM_list').items()
    for item in items:
        caipan = {
        'chengxu': item.find('.labelTwo').text(),
        'title': print(item.find("h4 a").text()),
        'fayuan': print(item.find(".slfyName").text()),
        'wenshuhao': print(item.find(".ah").text()),
        'date': print(item.find(".cprq").text()),
        'liyou': print(item.find("p").text())
    }
    browser.find_element_by_link_text('下一页').click()#点击下一页置换新页数据
    
url = 'http://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=8bc9a8bf1faf0a90b14f09ac1181182b&s8=02'
getUrl(url)
````
