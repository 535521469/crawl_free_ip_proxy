# encoding=utf8
'''
Created on 2013-4-24
@author: corleone
'''
from bot.const import HTTPProxyValueConst
from bot.dbitem import HTTPProxy
from bot.dbutil import FetchSession
from fiveone.items import IPProxyItem, HTTPProxyConst
from functools import wraps
import datetime
from scrapy import log

def save_item_2_db(parse):
    
    @wraps(parse)
    def simulate_parse(self, response):
        
        rss = parse(self, response)
        for rs in rss:
            fs = FetchSession()
            try:
                if isinstance(rs, IPProxyItem):
                    hp = fs.query(HTTPProxy).filter(HTTPProxy.ip == rs[HTTPProxyConst.ip].strip())\
                            .filter(HTTPProxy.procotol == rs[HTTPProxyConst.procotol].strip())\
                            .filter(HTTPProxy.port == rs[HTTPProxyConst.port].strip())\
                            .first()
                    if hp is None:
                        hp = HTTPProxy()
                        hp.ip = rs[HTTPProxyConst.ip].strip()
                        hp.port = rs[HTTPProxyConst.port].strip()
                        hp.procotol = rs[HTTPProxyConst.procotol].strip()
                        hp.fetcheddatetime = datetime.datetime.now()
                        hp.validflag = HTTPProxyValueConst.validflag_null
                        fs.add(hp)
                    else:
                        hp.fetcheddatetime = datetime.datetime.now()
                        hp.validflag = HTTPProxyValueConst.validflag_null
            except Exception as e:
                fs.rollback()
                self.log(u'save proxy 2 db error %s'%str(e),log.CRITICAL)
            else:
                fs.commit()
            finally:
                fs.close()
                    
    return simulate_parse
