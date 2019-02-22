# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):
    def process_item(self, item, spider):
        with open("result.txt", 'a', encoding='utf-8') as file:
            file.write(item['title'] + '\t' + item['cate'] + "\n")
