# encoding=utf8
'''
Created on 2013-4-10
@author: corleone
'''
from const import FetchProxySpiderConst, AppConst, ScrapyConst 
from multiprocessing.process import Process
from scrapy.cmdline import execute
from scrapy.settings import CrawlerSettings
import time
from bot.config import configdata
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

def fetch51nonanonymousfreeproxy():

    values = configdata.get(FetchProxySpiderConst.FetchFONonAnonymousProxySettings, {})
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
    execute(argv=["scrapy", "crawl", "FONonAnonymousSpider" ], settings=settings)

def fetch51anonymousfreeproxy():
    
    values = configdata.get(FetchProxySpiderConst.FetchFOAnonymousProxySettings, {})
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
    execute(argv=["scrapy", "crawl", "FOAnonymousSpider" ], settings=settings)
    
def build_process(target):
    f51fp = Process(target=target, name=target.__name__)
    f51fp.daemon = 1
    f51fp.start()
    return f51fp

def enqueue(target, p_dict):
    if target.__name__ not in p_dict or not p_dict[target.__name__].is_alive():
        p = build_process(target)
        p_dict[target.__name__] = p
    elif p_dict[target.__name__].is_alive():
        pass

if __name__ == '__main__':
    
    p_dict = {}
    frequence = configdata[AppConst.app_config].get(AppConst.app_config_frequence, 1800)
    frequence = int(frequence)
    while 1:
        enqueue(fetch51newfreeproxy, p_dict)
        enqueue(fetch51nonanonymousfreeproxy, p_dict)
        enqueue(fetch51anonymousfreeproxy, p_dict)
        print u'sleep %s seconds' % frequence
        time.sleep(frequence)
        
        
