# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from mySpider.items import BookItem
import urllib


class BookSpider(CrawlSpider):
    name = 'jingdong'
    allowed_domains = ['jd.com']
    start_urls = ['http://list.jd.com/list.html?cat=1713,3264,3414&ev=404_422171@&area=1,72,4137&page=1&delivery=0&stock=0&sort=sort_totalsales15_desc&plist=1&JL=6_0_0']
    rules = (
        Rule(LinkExtractor(allow='/list.html\?cat=1713,3264,3414&ev=404_422171@&area=1,72,4137&page=\d+&delivery=0&stock=0&sort=sort_totalsales15_desc&plist=1&JL=6_0_0'), callback='parse_item', follow='True'),
    )

    def parse_item(self, response):
        sel = Selector(response)
        sites = sel.xpath("//ul[@class='gl-warp clearfix']/li")
        items = []
        for site in sites:
            productid = site.xpath("div/div[2]/@data-sku").extract()
            priceUrl = 'http://p.3.cn/prices/mgets?skuIds=J_' + productid[0]
            price = []
            price.append(urllib.urlopen(priceUrl).read().split(',')[1][5:-1]) #这里写的很low

            item = BookItem()
            item['name'] = site.xpath("div/div[3]/a/em/text()").extract()
            item['price'] = price
            items.append(item)
        return items
    