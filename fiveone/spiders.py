# encoding=utf8
'''
Created on 2013-4-10
@author: corleone
'''
from fiveone.items import IPProxyItem, HTTPProxyConst
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from fiveone.tools import save_item_2_db

class FiveOneHomeSpider(BaseSpider):
    name = u"FiveOneHomeSpider"
    home_page = u'http://51dai.li/'

class FOSpider(FiveOneHomeSpider):
    name = u"FOSpider"
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
#                if country_td != u'CN':continue
                ipi = IPProxyItem()
                ipi[HTTPProxyConst.ip] = ip_td
                ipi[HTTPProxyConst.port] = port_td
                ipi[HTTPProxyConst.procotol] = u"http"
                yield ipi
                
        
    
    
