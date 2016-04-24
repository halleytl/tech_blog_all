# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import scrapy
from scrapy import Selector
from tech_blog_all.items import TechBlogAllItem

class MeituanSpider(scrapy.Spider):
    name = "meituan"
    allowed_domains = ["meituan.com"]
    start_urls = (
        'http://tech.meituan.com/archives',
    )

    def parse(self, response):
        sel = Selector(text = response.body)
        item = TechBlogAllItem()
        for page in sel.xpath("//article").extract():
            _sel = Selector(text= page)
            item["title"] = _sel.xpath("//header/a/text()").extract()[0]
            item["href"] = response.urljoin(_sel.xpath("//a/@href").extract()[0])
            print page
            author_items = _sel.xpath('//span[@class="post-meta-author"]/text()').extract()
            author = "作者未知"
            if author_items:
                author = author_items[0]
            item["author"] = author
            item["date"] = _sel.xpath('//span[@class="post-meta-ctime"]/text()').extract()[0]
            item["category"] = "暂时木有"
            yield item

