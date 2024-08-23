import scrapy
from scrapy_playwright.page import PageMethod


class LazadaspiderSpider(scrapy.Spider):
    name = "lazadaspider"
    allowed_domains = ["www.lazada.com.my", "scrapeops.io"]

    def start_requests(self):
        url = "https://www.lazada.com.my/tag/keychain/"
        yield scrapy.Request(
            url,
            meta=dict(
                playwright=True,
                playwright_include_page=True,
                PageMethods=[PageMethod("wait_for_selector", "div.ant-cole")],
                errback=self.error,
            ),
            callback=self.parse,
        )

    def parse(self, response):
        items = response.xpath('//div[contains(@class,"Bm3ON")]')
        print("***************************")
        print(items)
        print("***************************")

    async def error(self, faliure):
        page = faliure.request.meta["playwright"]
        await page.close
