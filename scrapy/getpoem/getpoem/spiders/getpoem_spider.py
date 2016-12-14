#coding=utf-8
import scrapy
from getpoem.items import GetpoemItem

class GetpoemSpider(scrapy.Spider):
    name = "getpoem"

    allowed_domain = "gushiwen.org"

    start_urls = [
            "http://so.gushiwen.org/type.aspx?p=1&x=%E8%AF%97"
            ]
    def parse(self, response):
        poem_list = response.xpath('//div[@class="sons"]')
        SITE_URL = "so.gushiwen.org"

        for poem in poem_list:
            item = GetpoemItem()
            item['name'] = poem.xpath('p[1]/a/text()').extract()
            item['info'] = poem.xpath('p[2]/text()').extract()
            item['content'] = poem.xpath('p[3]/text()').extract()
            href = poem.xpath('p[1]/a/@href').extract()
            item['href'] = response.urljoin(href[0])

            yield item
            print "href: %s", item['href']

        next_pages = response.xpath('//div[@class="pages"]/a[@style="width:60px;"]/@href').extract()
        if next_pages:
            next_page = response.urljoin(next_pages[0])
            #self.log('page_url: %s', next_page)
            yield scrapy.Request(next_page, self.parse)



