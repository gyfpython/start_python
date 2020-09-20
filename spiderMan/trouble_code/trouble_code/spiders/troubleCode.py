import os
import re

import scrapy
from urllib import parse


class WebSpider(scrapy.Spider):
    name = 'troublecodes'
    allowed_domains = ['troublecodes.net']

    def start_requests(self):
        urls = ['https://www.troublecodes.net/pcodes/']
        # urls = ['https://www.troublecodes.net/pcodes/', 'https://www.troublecodes.net/bcodes/',
        #         'https://www.troublecodes.net/ccodes/', 'https://www.troublecodes.net/ucodes/', ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        url_split = response.url.split('/')
        if not url_split[-1]:
            page = url_split[-2]
        else:
            page = url_split[-1]
        if page.endswith('.jpg') or page.endswith('.jpeg') or page.endswith('.png') or page.endswith('.css') or page.endswith('.js'):
            file_name = './resource/{}'.format(page)
            with open(file_name, 'wb') as f:
                f.write(response.body)
            return
        else:
            file_name = './resource/{}.html'.format(page)
            with open(file_name, 'wb') as f:
                f.write(response.body)
        self.log('Save file {}'.format(file_name))
        for href in response.xpath('//a/@href').getall():
            self.log('原始url：{}'.format(href))
            page_fixs = re.findall(r"(#.*?)/", href)
            for page_fix in page_fixs:
                href = href.replace(page_fix, '')
            page_fixs = re.findall(r"(#.*)", href)
            for page_fix in page_fixs:
                href = href.replace(page_fix, '')
            self.log('urljoin1之后：{}'.format(response.urljoin(href)))
            # yield scrapy.Request(response.urljoin(href), self.parse)


if __name__ == '__main__':
    test1 = '#100'
    print(re.findall(r"(#.*)", test1))