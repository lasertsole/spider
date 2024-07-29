import scrapy
import ddddocr
import random

from TaoSpider.items import TaospiderItem

class TaobaoSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = ["taobao.com"]
    tab = None

    def start_requests(self):
        keywords = ['手机']
        for keyword in keywords:
            for page in range(5):
                url = f"https://s.taobao.com/search?q={keyword}&page={page}"
                yield scrapy.Request(url=url)

    def parse(self, response):
        tab = self.tab
        tab.wait.load_start()

        try:
            if tab.ele("x://div[@class='nc_wrapper']"):
                for _ in range(3):
                    # wrapper_width = tab.run_js("document.querySelector('.nc_wrapper').offsetWidth", as_expr=True)
                    # slider_width = tab.run_js("document.querySelector('.btn_slide').offsetWidth", as_expr=True)
                    # need_move = wrapper_width - slider_width
                    slider_dom = tab.ele("x://span[@id='nc_1_n1z']")
                    tab.actions.hold(slider_dom)
                    tab.actions.move(offset_x=270, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.2)
                    tab.actions.release(slider_dom)
                    if tab.ele("x://div[@class='errloading']"):
                        tab.ele("x://div[@class='errloading']").click()

            blanks = tab.eles("x://a[@target='_blank' and starts-with(@class,'Card--doubleCardWrapper')]")
            for blank in blanks:
                item = TaospiderItem()
                item['title'] = blank.ele("x:.//div[starts-with(@class,'Title--title')]//span").text
                item['price'] = blank.ele("x:.//div[starts-with(@class, 'Price')]//div").text
                item['deal_count'] = blank.ele("x:.//span[starts-with(@class, 'Price--realSales')]").text
                item['shop'] = blank.ele("x:.//a[starts-with(@class, 'ShopInfo--shopName')]").text
                item['location'] = blank.ele("x:.//div[starts-with(@class, 'Price--procity')]/span").text
                print(item)
        except Exception as e:
            print("爬取失败"+str(e))
        finally:
            tab.close()
