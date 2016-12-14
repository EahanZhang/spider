#coding=utf-8

import scrapy
from news163.items import News163Item
import num

import sys
reload(sys)
sys.setdefaultencoding('gb18030')

class News163Spider(scrapy.Spider):
    name = "news163"
    domain = "sina.com.cn"
    start_urls = [
            "http://roll.news.sina.com.cn/"
            ]

    def parse(self, response):
        url = "http://roll.news.sina.com.cn/s/channel.php?ch=01#col=89&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page="
        for rel in response.xpath('//ul/li'):
            item = News163Item()
            item['programa'] = rel.xpath('span[@class="c_chl"]/a/text()').extract()
            item['title'] = rel.xpath('span[@class="c_tit"]/a/text()').extract()
            item['href'] = rel.xpath('span[@class="c_tit"]/a/@href').extract()
            item['date'] = rel.xpath('span[@class="c_time"]/text()').extract()
            yield item
        """
        num.NUM = num.NUM + 1

        if num.NUM <= 275:
            new_url = url + str(num.NUM)
            yield scrapy.Request(new_url, self.parse)
        """

        num = 1

        while num <=275:
            new_url = url + str(num)
            yield scrapy.Request(new_url, self.parse)
            num = num + 1
