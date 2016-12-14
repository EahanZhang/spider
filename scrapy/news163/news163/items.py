import scrapy

class News163Item(scrapy.Item):
    programa = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    href = scrapy.Field()
