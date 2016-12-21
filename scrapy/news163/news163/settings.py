# -*- coding: utf-8 -*-

# Scrapy settings for news163 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'news163'

SPIDER_MODULES = ['news163.spiders']
NEWSPIDER_MODULE = 'news163.spiders'

DEPTH_LIMIT = 2
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'news163 (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
        'news163.pipelines.News163Pipeline' : 300
}

DB_HOST = "127.0.0.1"
DB_PORT = 27017
DB_NAME = "mydb"
DB_DOCNAME = "news163"
