import scrapy
from Movie250.items import Movie250Item

class Movie250Spider(scrapy.Spider):
    #docstring for Movie250Spider
    name = "movie250"
    allowed_domain = "douban.com"
    start_urls = [
            "http://movie.douban.com/top250/"
    ]

    def parse(self, response):
        for rel in response.xpath('//div[@class="item"]'):
            item = Movie250Item()
            item['rank'] = rel.xpath('div[@class="pic"]/em/text()').extract().encode('utf-8')
            item['title'] = rel.xpath('div[@class="pic"]/a/img/@alt').extract().encode('utf-8')
            item['link'] = rel.xpath('div[@class="pic"]/a/@href').extract().encode('utf-8')
            item['star'] = rel.xpath('div[@class="info"]/div[@class="bd"/div[@class="star"]/span[@class=rating_num]/text()]')
            item['rate'] = rel.xpath('div[@class="info"]/div[@class="bd"/div[@class="star"]/span/text()')
            item['quote'] = rel.xpath('div[@class="info"]/div[@class="bd"/p[@class="quote"]/span/text()')

            yield item

        next_page = response.xpath('//span[@class="next"]/a/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)
