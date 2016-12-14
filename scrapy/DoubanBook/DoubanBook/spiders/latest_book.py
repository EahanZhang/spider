import scrapy

class DoubanbookSpider(scrapy.Spider):
    name = "latestbook"
    allowed_domain = "douban.com"
    start_urls = [
            "https://book.douban.com/latest?icn=index-latestbook-all"
    ]

    def parse(self, response):
        detail = reponse.xpath("//ul/li")
        
        for sel in detail:
            name = sel.xpath("/div/h2/text()").extract()
            print name

