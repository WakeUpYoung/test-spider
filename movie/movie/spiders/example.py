# -*- coding: utf-8 -*-
import scrapy

from movie.items import MovieItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://meijutt.com/new100.html']

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        # movies = response.xpath('/html/body/div[3]/div[4]/div[1]/ul/li')
        for each_movie in movies:
            item = MovieItem()
            item['title'] = each_movie.xpath('./h5/a/@title').extract()[0]
            item['cate'] = each_movie.xpath('./span[@class="mjjq"]/text()').extract()[0]
            yield item
        pass
