# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from news163 import settings
import pymongo

class News163Pipeline(object):
    def __init__(self):
        #self.file = codecs.open('scraped_data_utf8.json', 'w', encoding='utf-8')'''''')
        host = settings.DB_HOST
        port = settings.DB_PORT
        dbname = settings.DB_NAME
        docname = settings.DB_DOCNAME
        client = pymongo.MongoClient(host=host, port=port) #connect to mongodb
        tdb = client[dbname] #get the database named [@dbname]
        self.post = tdb[docname] #open or create the table named [@docname]

    def process_item(self, item, spider):
        #line = json.dumps(dict(item), ensure_ascii=False) + "\n"""
        #self.file.write(line)
        info = dict(item)
        self.post.insert(info)
        return item

    def spider_closed(self, spider):
        self,file,close()
