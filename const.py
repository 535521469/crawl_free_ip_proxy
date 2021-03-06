# encoding=utf8
'''
Created on 2013-4-26
@author: corleone
'''
class ScrapyConst(object):
    BOT_NAME = u'BOT_NAME'
    SPIDER_MODULES = u'SPIDER_MODULES'
    LOG_LEVEL = u'LOG_LEVEL'
    LOG_FILE = u'LOG_FILE'
    DOWNLOAD_TIMEOUT = u'DOWNLOAD_TIMEOUT'
    Console = u'Console'
    RETRY_TIMES = u'RETRY_TIMES'
    LOG_DIR = u'LOG_DIR'

class FetchProxySpiderConst(ScrapyConst):
    FetchProxySettings = u'fetch51newproxysettings'
    FetchFOAnonymousProxySettings = u'fetch51anonymousproxysettings'
    FetchFONonAnonymousProxySettings = u'fetch51nonanonymousproxysettings'

class ValidProxySpiderConst(ScrapyConst):pass

class AppConst(object):
    app_config = u'app'
    app_config_frequence=u'frequence'