import scrapy
import re
import json
#import logging

class QuotesSpider(scrapy.Spider):
    name = 'links'
    start_urls = ['https://www.fastfloors.com']

    def __init__(self):
        self.links=[]

    def parse(self, response):
        self.links.append(response.url)
        for href in response.css('a::attr(href)'):
            yield response.follow(href, self.parse)