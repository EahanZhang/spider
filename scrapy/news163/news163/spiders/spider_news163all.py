#coding=utf-8

import scrapy
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.linkextractors import LinkExtractor
from news163.items import News163Item
from scrapy.contrib.spiders import CrawlSpider,Rule
import re

class News163allSpider(CrawlSpider):
    name = "news163all"   #spider name

    allowed_domains = "sina.com.cn"
    start_urls = [
            "http://roll.news.sina.com.cn/s/channel.php?ch=01#col=89&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page=1",
            "http://roll.news.sina.com.cn"
            ]

    rules = ( 
        Rule(LinkExtractor(allow=('s/channel.php\?ch\=01#col\=89&spec\=&type\=&ch\=01&k\=&offset_page\=0&offset_num\=0&num\=60&asc\=&page\=([\d]+)', ),),callback='parse_item', follow='true'),
    )   #make rules

    def parse_item(self, response):
        sel = response.selector
        #items = [] 
        path = response.xpath('//ul/li')

        for rel in response.xpath('//ul/li'):
            item = News163Item()
            item['programa'] = rel.xpath('span[@class="c_chl"]/a/text()').extract()
            item['title'] = rel.xpath('span[@class="c_tit"]/a/text()').extract()
            item['href'] = rel.xpath('span[@class="c_tit"]/a/@href').extract()
            item['date'] = rel.xpath('span[@class="c_time"]/text()').extract()
            yield item


