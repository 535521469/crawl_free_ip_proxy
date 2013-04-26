# encoding=utf8
'''
Created on 2013-4-10
@author: corleone
'''
from fiveone.items import IPProxyItem, HTTPProxyConst
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy import log
from fiveone.tools import save_item_2_db

class FiveOneHomeSpider(BaseSpider):
    name = u"FiveOneHomeSpider"
    home_page = u'http://51dai.li/'

class FiveOneNewHTTPProxySpider(FiveOneHomeSpider):
    
    name = u"FiveOneNewHTTPProxySpider"
    
    start_urls = [
                  u'%shttp_fast.html' % FiveOneHomeSpider.home_page,
                  #=============================================================
                   u'%shttp_anonymous.html' % FiveOneHomeSpider.home_page,
                   u'%shttp_non_anonymous.html' % FiveOneHomeSpider.home_page,
                  #=============================================================
                  ]
    
    @save_item_2_db
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        tb_tags = hxs.select(u'//div[@id="tb"]/table')
        
        for tr_tag in tb_tags.select('tr'):
            
            td_tags = tr_tag.select('td/text()').extract()
            if td_tags:
                idx_td, ip_td, port_td, country_td = td_tags
                ipi = IPProxyItem()
                ipi[HTTPProxyConst.ip] = ip_td
                ipi[HTTPProxyConst.port] = port_td
                ipi[HTTPProxyConst.procotol] = u"http"
                
                http_msg = u"%s://%s:%s" % (ipi[HTTPProxyConst.procotol], ip_td, port_td)
                self.log(http_msg, log.INFO)
                
                with open(u'proxy.txt', u'a') as f:
                    f.write(http_msg + u'\n')
                
                yield ipi
                
class BaiDuHomePageSpider(BaseSpider):
    
    name = u'BaiDuHomePageSpider'
    
    def start_requests(self):
        
        proxies = []
        with open(u'proxy.txt', u'r') as f:
            proxies = map(str.strip, f.readlines())
        
        for proxy in proxies:
            yield Request(u'http://www.baidu.com',
                          meta={u'proxy':proxy},
                          dont_filter=True)
        
    
    def parse(self, response):
        
        meta = response.request.meta
        with open(u'enable_proxies.txt', u'a')as f:
            f.write(meta[u'proxy'] + u'\n')
        
    
    
