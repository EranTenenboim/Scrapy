import scrapy
import re
import json
#import logging

class QuotesSpider(scrapy.Spider):
    name = 'data_info'
    start_urls = ['https://www.fastfloors.com/bamboo/blue-forest/engineered-click-lock-4-15-16/champagne/index.asp',
                  'https://www.fastfloors.com/bamboo/blue-forest/engineered-click-lock-4-15-16/tawny/index.asp']

    def parse(self, response):                                             
       prod=self.create_info(response)
       return prod
      

    def create_info(self,response):
        
        info = {}
        
        info['title']= response.css('title::text').get() 
        info['name']=response.xpath('//div[@id="seriesName"]/text()').get()
        info['image']=response.xpath('//div[@id="productMainImage"]/p/a/img/@src').extract()
        
        product_headers=response.xpath('//div[@class="productDetailSpecLabel specLabel-6"]/text()').extract()
        products_data= response.xpath('//div[@class="productDetailSpec spec-6"]/text()').extract()

        datacounter=1
        for i in range(1,len(product_headers)-1):
            info[product_headers[i]]=products_data[datacounter]

            while ('\xa0or' in products_data[datacounter]):  
                #self.log(products_data[datacounter])
                datacounter+=1
                info[product_headers[i]] +=products_data[datacounter]

            info[product_headers[i]] = info[product_headers[i]].replace('\n','').replace('\xa0',' ')
            datacounter+=1

        return info