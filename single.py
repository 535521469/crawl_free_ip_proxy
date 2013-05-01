# encoding=utf8
'''
Created on 2013-4-10
@author: corleone
'''
from bot.config import configdata
from const import FetchProxySpiderConst, ScrapyConst
from scrapy.cmdline import execute
from scrapy.settings import CrawlerSettings
import os

def fetch51newfreeproxy():
    
    values = configdata.get(FetchProxySpiderConst.FetchProxySettings, {})
    values[ScrapyConst.DOWNLOAD_TIMEOUT] = int(values.get(ScrapyConst.DOWNLOAD_TIMEOUT, 0))
    if ScrapyConst.Console in values:
        if values[ScrapyConst.Console] == u'1':# out to console
            values[ScrapyConst.LOG_FILE] = None
        else:
            log_dir = values.get(ScrapyConst.LOG_DIR, os.getcwd())
            if ScrapyConst.LOG_FILE in values:
                log_file = values[ScrapyConst.LOG_FILE]
                values[ScrapyConst.LOG_FILE] = os.sep.join([log_dir , log_file])
                
    settings = CrawlerSettings(None, values=values)
    execute(argv=["scrapy", "crawl", "FONEWSpider" ], settings=settings)

if __name__ == '__main__':
    
    fetch51newfreeproxy()
    
