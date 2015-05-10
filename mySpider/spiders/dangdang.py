# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from mySpider.items import BookItem


class BookSpider(CrawlSpider):
    name = 'dangdang'
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cp01.25.01.03.00.00.html']
    rules = (
        Rule(LinkExtractor(allow='/pg\d+-cp01\.25\.01\.03\.00\.00\.html'), callback='parse_item', follow='True'),
    )

    def parse_item(self, response):
        sel = Selector(response)
        sites = sel.xpath("//ul[@class='list_aa listimg']/li")
        items = []
        for site in sites:
            item = BookItem()
            item['name'] = site.xpath("div/a/@title").extract()
            item['price'] = site.xpath("div/p[@class='price']/span[@class='price_n']/text()").extract()
            items.append(item)
        return items
