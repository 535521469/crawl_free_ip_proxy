# encoding=utf8
'''
Created on 2013-4-10
@author: corleone
'''
from bot.config import configdata
from const import FetchProxySpiderConst
from scrapy.cmdline import execute
from scrapy.settings import CrawlerSettings

def fetch51freeproxy():
    values = configdata.get(FetchProxySpiderConst.FetchProxySettings, {})
    settings = CrawlerSettings(values=values)
    execute(argv=["scrapy", "crawl", "FOSpider" ], settings=settings)
        
if __name__ == '__main__':
    
    fetch51freeproxy()
    
    


