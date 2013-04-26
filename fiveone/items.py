# encoding=utf8
'''
Created on 2013-4-10
@author: corleone
'''
from scrapy.item import Item, Field

class IPProxyItem(Item):

#===============================================================================
# CREATE TABLE `HTTPProxy` (
#  SEQID varchar(32) NOT NULL COMMENT '记录ID',
#  Procotol varchar(32) not null comment '协议类型',
#  IP varchar(256) not null COMMENT 'IP地址',
#  Port VARCHAR(16) NOT NULL COMMENT '端口',
#  ValidDateTime datetime default null comment '验证有效时间',
#  ValidFlag varchar(4) not null comment '有效标识|0:无效;1:有效;2未验证',
#  primary key (SEQID)  
#  )ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='代理信息';
#===============================================================================


    procotol = Field()
    ip = Field()
    port = Field()

class HTTPProxyConst(object):
    
    ip = u'ip'
    port = u'port'
    procotol = u'procotol'

    
