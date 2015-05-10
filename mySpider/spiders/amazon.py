# -*- coding: utf-8 -*-

from scrapy import Spider, Selector
from scrapy.http import Request
from mySpider.items import BookItem


class BookSpider(Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.cn']
    start_urls = [] #http://www.amazon.cn/s/ref=sr_pg_2?fst=as%3Aoff&rh=n%3A658390051%2Cn%3A%21658391051%2Cn%3A658399051%2Cn%3A658579051%2Cn%3A659656051&page=2&bbn=658579051&ie=UTF8&qid=1428679737
    u1 = 'http://www.amazon.cn/s/ref=sr_pg_'
    u2 = '?fst=as%3Aoff&rh=n%3A658390051%2Cn%3A%21658391051%2Cn%3A658399051%2Cn%3A658579051%2Cn%3A659656051&page='
    u3 = '&bbn=658579051&ie=UTF8&qid=1428683135'
    for i in range(101):
        url = u1 + str(i+1) + u2 + str(i+1) + u3
        start_urls.append(url)

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath("//ul[@id='s-results-list-atf']/li")
        items = []
        for site in sites:
            item = BookItem()
            item['name'] = site.xpath("div/div/div/div[2]/div[1]/a/h2/text()").extract()
            item['price'] = site.xpath("div/div/div/div[2]/div[2]/div[1]/div[2]/a/span/text()").extract()
            items.append(item)
        return items
    