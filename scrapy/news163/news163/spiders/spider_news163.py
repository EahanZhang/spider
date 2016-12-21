#coding=utf-8

import scrapy
from news163.items import News163Item

class News163Spider(scrapy.Spider):
    name = "news163"
    domain = "sina.com.cn"
    start_urls = [
            "http://roll.news.sina.com.cn/s/channel.php?ch=01#col=89&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page=1"
            ]
    url = "http://roll.news.sina.com.cn/s/channel.php?ch=01#col=89&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page="
    i = 2
    while i < 275:
        new_url = url + str(i)
        start_urls.append(new_url)
        i = i + 1

    def parse(self, response):
        for rel in response.xpath('//div[@id="d_list"]/ul/li'):
            item = News163Item()
            title = rel.xpath('span[@class="c_tit"]/a/text()').extract()
            item['title'] = title[0].encode('utf-8')
            item['href'] = rel.xpath('span[@class="c_tit"]/a/@href').extract()
            item['date'] = rel.xpath('span[@class="c_time"]/text()').extract()
            print "---------------%s", item['title']
            yield item
        """
        num.NUM = num.NUM + 1

        if num.NUM <= 275:
            new_url = url + str(num.NUM)
            yield scrapy.Request(new_url, self.parse)
        i = 2
        pages = []
        url = "http://roll.news.sina.com.cn/s/channel.php?ch=01#col=89&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page="
        while i <= 275:
            #get next page
            next_page = url + str(i)
            pages.append(next_page)
            i = i + 1
            print "---------------------------next_page: %s", next_page

        for page in pages:
            #print page
            yield scrapy.Request(page, self.parse_content)
        """
    '''
    def parse_content(self, response):
        print "-------------simple--------------------"
        for rel in response.xpath('//div[@id="d_list"]/ul/li'):
            item = News163Item()
            title = rel.xpath('span[@class="c_tit"]/a/text()').extract()
            item['title'] = title[0].encode('utf-8')
            item['href'] = rel.xpath('span[@class="c_tit"]/a/@href').extract()
            item['date'] = rel.xpath('span[@class="c_time"]/text()').extract()
            print "---------------%s", item['href']
            yield item
            '''
