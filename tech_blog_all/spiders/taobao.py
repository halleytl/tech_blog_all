# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Selector, Request
from tech_blog_all.items import TechBlogAllItem


class TaobaoSpider(Spider):
    name = "taobao"
    allowed_domains = ["taobao.org"]
    start_urls = (
        'http://jm.taobao.org/',
    )


    def parse(self, response):
        sel = Selector(text = response.body)
        item = TechBlogAllItem()
        for page in sel.xpath("//article").extract():
            _sel = Selector(text= page)
            item["title"] = _sel.xpath("//header//a/text()").extract()[0].strip()
            item["href"] = response.urljoin(_sel.xpath('//a[@class="post-title-link"]/@href').extract()[0])
            author = "作者未知"
            item["author"] = author
            item["date"] = _sel.xpath('//time/text()').extract()[0].strip()
            #<span itemprop="name">消息中间件</span>
            item["category"] = _sel.xpath('//span[@itemprop="name"]/text()').extract()[0]
            yield item
        next_page = sel.xpath('//a[@class="extend next"]/@href').extract()
        if next_page:
            yield Request(response.urljoin(next_page[0]), self.parse)



