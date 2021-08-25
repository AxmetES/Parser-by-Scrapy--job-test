import os
from urllib.parse import urlparse, urljoin

import scrapy
from environs import Env

env = Env
env.read_env()


class KolesaSpiderSpider(scrapy.Spider):
    name = 'kolesa_spider'
    parts = urlparse(os.getenv('SITE_URL'))
    main_url = parts.scheme + '://' + parts.netloc

    start_urls = [os.getenv('SITE_URL')]

    def parse(self, response):
        for car_div in response.css('div.a-elem'):
            title = car_div.css('a.ddl_product_link::text').get()
            price = car_div.css('span.price::text').get()
            link = urljoin(self.main_url, car_div.css('a.ddl_product_link').attrib['href'])

            yield {'title': title,
                   'price': (price.replace(u'\xa0', u' ')).strip('\n').strip(),
                   'link': link,
                   }

        next_page = response.css('a.right-arrow.next_page').attrib['href']
        if next_page:
            url = urljoin(self.main_url, next_page)
            yield response.follow(url, callback=self.parse)