# -*- coding: utf-8 -*-

# Scrapy settings for Movie250 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Movie250'

SPIDER_MODULES = ['Movie250.spiders']
NEWSPIDER_MODULE = 'Movie250.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Movie250 (+http://www.yourdomain.com)'

HEADER = {
"Host":"movie.douban.com",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding":"gzip, deflate, br",
"Connection":"keep-alive",
"Upgrade-Insecure-Requests":"1",
"Cache-Control":"max-age=0",
}

COOKIES = {
'll':r'"108288"',
'bid':r'H7Ea7rPKJW0',
'__utma':r'30149280.1940774216.1481767311.1481767311.1481767311.1',
'__utmb':r'30149280.5.10.1481767311',
'__utmz':r'30149280.1481767311.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
'__utmc':r'30149280',
'__utmt':r'1',
'_pk_id.100001.4cf6':r'787a0a3109137b45.1481768664.1.1481768664.1481768664.',
'_pk_ses.100001.4cf6':r'*',
'__utma':r'223695111.1128651840.1481768664.1481768664.1481768664.1',
'__utmb':r'223695111.0.10.1481768664',
'__utmc':r'223695111',
'__utmz':r'223695111.1481768664.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
}

