import os
from urllib.parse import urlparse, urljoin

import scrapy
from environs import Env

env = Env
env.read_env()


class KolesaSpiderSpider(scrapy.Spider):
    """Паук парсер"""
    name = 'kolesa_spider'
    parts = urlparse(
        os.getenv('SITE_URL',
                  'https://kolesa.kz/cars/vaz/nur-sultan/?auto-car-transm=2345'))

    main_url = parts.scheme + '://' + parts.netloc  # Востановление адреса главной страницы сайта.

    start_urls = [
        os.getenv('SITE_URL',
                  'https://kolesa.kz/cars/vaz/nur-sultan/?auto-car-transm=2345')]

    def clean_price(self, text):
        """Очистка переменной "цена" от лишних символов и пробелов."""
        digits = [symbol for symbol in text if symbol.isdigit()]
        clean_digits = ''.join(digits)
        return clean_digits

    def parse_2(self, response):
        """Дополнительная функция для парсинга ссылок на фотографии на странице обявления."""

        images = []
        images.clear()
        item = response.meta['item']
        for pic in response.css('.gallery__thumb'):
            images.append(pic.css('.js__gallery-thumb').attrib['data-href'])
        item['image'] = images
        yield item

    def parse(self, response):
        """Первичная функция для парсинга обьявлении."""
        for car_div in response.css('div.a-elem'):
            title = car_div.css('a.ddl_product_link::text').get()
            price = car_div.css('span.price::text').get()
            link = urljoin(self.main_url, car_div.css('a.ddl_product_link').attrib['href'])

            item = {'title': title,
                    'price': self.clean_price(price),
                    'link': link,
                    }
            if link is not None:
                yield scrapy.Request(link, callback=self.parse_2, meta={'item': item})

        next_page = response.css('a.right-arrow.next_page').attrib['href']
        if next_page:
            url = urljoin(self.main_url, next_page)
            yield response.follow(url, callback=self.parse)
