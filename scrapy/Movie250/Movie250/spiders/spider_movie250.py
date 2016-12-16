#coding=utf-8
#author=sunshine

import scrapy
from Movie250.items import Movie250Item
from Movie250 import settings
import time
import urlparse

class Movie250Spider(scrapy.Spider):
    #docstring for Movie250Spider
    name = "movie250"
    allowed_domain = "douban.com"
    '''
    start_urls = [
            "http://movie.douban.com/top250/"
    ]
    '''

    def start_requests(self):
        return [scrapy.FormRequest("https://movie.douban.com/top250/", \
                headers = settings.HEADER, \
                cookies = settings.COOKIES, \
                callback = self.parse)]

    def parse(self, response):
        print response.url
        for rel in response.xpath('//div[@class="item"]'):
            item = Movie250Item()
            item['rank'] = rel.xpath('div[@class="pic"]/em/text()').extract()
            item['title'] = rel.xpath('div[@class="pic"]/a/img/@alt').extract()
            item['link'] = rel.xpath('div[@class="pic"]/a/@href').extract()
            item['star'] = rel.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            item['rate'] = rel.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[4]/text()').extract()
            item['quote'] = rel.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span[1]/text()').extract()
            yield item

        time.sleep(1)
        next_pages = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_pages:
            url = urlparse.urljoin(response.url, next_pages[0])
            print "---------------url: %s", url
            yield scrapy.Request(\
                    url, \
                    self.parse,\
                    headers = settings.HEADER, \
                    cookies = settings.COOKIES\
                    )
