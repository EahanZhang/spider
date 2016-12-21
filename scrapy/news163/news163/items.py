import scrapy

class News163Item(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    href = scrapy.Field()
