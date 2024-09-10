import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class EmailSpider(CrawlSpider):
    name = 'email_spider'
    
    def __init__(self, start_url=None, *args, **kwargs):
        super(EmailSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url] if start_url else []
        self.allowed_domains = [self.start_urls[0].split("//")[-1].split("/")[0]]

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # Extract emails from the current page
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', response.text)
        
        for email in emails:
            yield {'email': email}
