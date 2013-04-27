# encoding=utf8
'''
Created on 2013-4-24
@author: corleone
'''
from bot.const import HTTPProxyValueConst as vc
from bot.dbitem import HTTPProxy
from bot.dbutil import FetchSession
from fiveone.items import IPProxyItem, HTTPProxyConst
from functools import wraps
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
                        hp.validflag = vc.validflag_null
                        fs.add(hp)
                        msg = (u'++ %s %s:%s' % (hp.procotol,
                                                             hp.ip, hp.port))
                        self.log(msg, log.INFO)
                    else:
                        if unicode(hp.validflag) != vc.validflag_no:
                            msg = (u'** %s %s:%s %s to '
                                   '%s' % (hp.procotol, hp.ip, hp.port,
                                         hp.validflag, vc.validflag_null))
                            hp.validflag = vc.validflag_null
                            self.log(msg, log.INFO)
                            
            except Exception as e:
                fs.rollback()
                self.log(u'save proxy 2 db error %s' % str(e), log.CRITICAL)
            else:
                fs.commit()
            finally:
                fs.close()
                    
    return simulate_parse
