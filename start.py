# encoding=utf8
'''
Created on 2013-4-10
@author: corleone
'''
from bot.configutil import ConfigFile
from const import FetchProxySpiderConst, AppConst
from multiprocessing.process import Process
from scrapy.cmdline import execute
from scrapy.settings import CrawlerSettings
import os
import time
from bot.config import configdata

def fetch51freeproxy():
    configdata = ConfigFile.readconfig(os.sep.join([os.path.curdir, 'fetchproxy.cfg']))
    values = configdata.get(FetchProxySpiderConst.FetchProxySettings, {})
    settings = CrawlerSettings(values=values)
    execute(argv=["scrapy", "crawl", "FOSpider" ], settings=settings)

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
    print frequence
    frequence = int(frequence)
    while 1:
        enqueue(fetch51freeproxy, p_dict)
        time.sleep(frequence)

#    print f51fp.daemon
#    f51fp.join()
    
    
    


