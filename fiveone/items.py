# encoding=utf8
'''
Created on 2013-4-10
@author: corleone
'''
from scrapy.item import Item, Field

class IPProxyItem(Item):
    
    procotol = Field()
    ip = Field()
    port = Field()

class HTTPProxyConst(object):
    
    ip = u'ip'
    port = u'port'
    procotol = u'procotol'

    
