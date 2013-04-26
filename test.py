# encoding=utf8
'''
Created on 2013-4-10
@author: corleone
'''
from scrapy.settings import CrawlerSettings
from scrapy.cmdline import execute
from bot.configutil import ConfigFile
from const import FetchProxySpiderConst
import os

def fetch51freeproxy():
    configdata = ConfigFile.readconfig(os.sep.join([os.path.curdir, 'fetchproxy.cfg']))
    values = configdata.get(FetchProxySpiderConst.FetchProxySettings, {})
    settings = CrawlerSettings(values=values)
    execute(argv=["scrapy", "crawl", "FOSpider" ], settings=settings)
        
if __name__ == '__main__':
    
    fetch51freeproxy()
    
    


