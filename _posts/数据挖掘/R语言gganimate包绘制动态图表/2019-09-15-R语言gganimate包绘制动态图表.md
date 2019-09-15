---
published: true
layout: post
title: R语言gganimate包绘制动态图表
date: '2019-09-15 20:39:00 +0800'
categories: R语言
---

![](https://raw.githubusercontent.com/lvxiong7zg/lvxiong7zg.github.io/master/_posts/%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98/R%E8%AF%AD%E8%A8%80gganimate%E5%8C%85%E7%BB%98%E5%88%B6%E5%8A%A8%E6%80%81%E5%9B%BE%E8%A1%A8/%E6%95%A3%E7%82%B9%E5%8A%A8%E6%80%81%E5%9B%BE.gif)

>代码：

<!-- more -->
```YMAL
library(gapminder)
library(ggplot2)
library(gganimate)
theme_set(theme_bw())

##示例1 散点动态图
head(gapminder)
tail(gapminder)
ggplot(gapminder, aes(gdpPercap, lifeExp, size = pop, colour = country)) +
  geom_point(alpha = 0.7, show.legend = FALSE) +
  scale_colour_manual(values = country_colors) +        #进行数值之间的映射
  scale_size(range = c(2, 12)) +                    #设置绘图符号大小
  scale_x_log10() +                              #连续数据位置的标准化
  facet_wrap(~continent) +                     #按照continent进行分类
  # Here comes the gganimate specific bits
  labs(title = 'Year: {frame_time}', x = 'GDP per capita', y = 'life expectancy') +
  transition_time(year) +
  ease_aes('linear')#指数据变化的状态，线性发展比较缓慢




##示例2 箱线动态图

ggplot(mtcars, aes(factor(cyl), mpg)) +
  geom_boxplot() + geom_point() +
  transition_states(  
    gear, 
    transition_length = 2,
    state_length = 1
  ) +
  enter_fade() +
  exit_shrink() +
  ease_aes('sine-in-out')
````

![](https://raw.githubusercontent.com/lvxiong7zg/lvxiong7zg.github.io/master/_posts/%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98/R%E8%AF%AD%E8%A8%80gganimate%E5%8C%85%E7%BB%98%E5%88%B6%E5%8A%A8%E6%80%81%E5%9B%BE%E8%A1%A8/%E7%AE%B1%E7%BA%BF%E5%8A%A8%E6%80%81%E5%9B%BE.gif)


![原文http://www.sohu.com/a/336347406_718302](http://www.sohu.com/a/336347406_718302)
