# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


def get_cookies_dict(cookies_str):
    cookies_dict = {}
    for cookie in cookies_str.split(';'):
        cookie = cookie.strip()
        key, value = cookie.split('=', maxsplit=1)
        cookies_dict[key] = value
    return cookies_dict

COOKIES_DICT = get_cookies_dict('bid=h0v3Y3AerrE; __utma=30149280.420961230.1721930164.1721930164.1721930164.1; __utmb=30149280.0.10.1721930164; __utmc=30149280; __utmz=30149280.1721930164.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.818134026.1721930164.1721930164.1721930164.1; __utmb=223695111.0.10.1721930164; __utmc=223695111; __utmz=223695111.1721930164.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _pk_id.100001.4cf6=15e4fe89178a071e.1721930164.; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __yadk_uid=NjLVM19p2z5X3SHqMuCCI60MvDmXYEJ9; ll="118291"; _vwo_uuid_v2=DD9665C27BD43A7D189F59CC3CBF33A7B|f0c3fd15d378e7f5094ce9f0419266a8')

class Spider2107SpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class Spider2107DownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        request.cookies = COOKIES_DICT
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
