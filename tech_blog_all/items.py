# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TechBlogAllItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题
    title = scrapy.Field()
    # 连接地址
    href = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # 分类
    category = scrapy.Field()
