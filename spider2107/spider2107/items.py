# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#爬虫爬到的数据封装成item
class MovieItem(scrapy.Item):
    title = scrapy.Field()
    rank = scrapy.Field()
    subject = scrapy.Field()
