# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import csv


reload(sys)
sys.setdefaultencoding('utf-8')

class CsvWriterPipeline(object):
    def __init__(self):
        self.csvfile = open('book.csv', 'wb')
    
    def process_item(self, item, spider):
        temp = []
        spamwriter = csv.writer(self.csvfile, dialect='excel')
        temp.append(item['name'][0].encode('gbk', 'ignore'))
        temp.append(item['price'][0].encode('gbk', 'ignore'))
        spamwriter.writerow(temp)
        return item