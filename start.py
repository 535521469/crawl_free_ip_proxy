# encoding=utf8
'''
Created on 2013-4-10
@author: corleone
'''
from scrapy.settings import CrawlerSettings
from scrapy.cmdline import execute

if __name__ == '__main__':
    module_ = __import__('fiveone.settings', {}, {}, [''])
    settings = CrawlerSettings(module_,)
    execute(argv=["scrapy", "crawl", "FiveOneNewHTTPProxySpider" ], settings=settings)

