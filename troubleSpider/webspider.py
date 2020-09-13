import logging
import os
import re

import requests
from threading import Thread
import threading

all_url = set()


class WebSpider(object):

    def __init__(self, host):
        self.base_url = 'https://' + host
        self.host = host
        self.fetch_role = '(src|href)=(\'|\")(.*?)(\"|\')'

    def login(self):
        pass

    def logout(self):
        pass

    def get_page(self, url: str):
        global all_url
        if url in all_url:
            return
        all_url.add(url)
        print('当前爬取页面总数：{}'.format(len(all_url)))
        print('start spider {}'.format(url))
        headers = {
            'user-agent': 'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/79.0.3945.88Safari/537.36',
            'accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, image/apng, */*;q=0.8, application/signed-exchange;v = b3;q = 0.9',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'zh-CN, zh;q=0.9, en;q=0.8',
            'Host': self.host,
            'cache-control': 'max-age=0',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'upgrade-insecure-requests': '1'
        }
        get_success =  False
        for i in range(5):
            try:
                response = requests.get(url=url, headers=headers, timeout=20)
                if url.endswith('.gif') or url.endswith('.png') or url.endswith('.jpg') or url.endswith('.jpeg'):
                    file_name = self.transform_url_to_path(url)
                    if not os.path.isdir(os.path.dirname(file_name)):
                        os.makedirs(os.path.dirname(file_name))
                    with open(file_name, 'wb') as f:
                        f.write(response.content)
                    print('end spider {}'.format(url))
                    get_success = True
                    break
                if url.endswith('.js') or url.endswith('.css'):
                    self.save_to_html([], url, response.text)
                    get_success = True
                    break
                changed_url = self.fetch_url(response.text, url)
                self.save_to_html(changed_url, url, response.text)
                print('end spider {}'.format(url))
                for url_tem in changed_url:
                    self.get_page(url_tem['request_url'])
                get_success = True
                break
            except Exception as e:
                logging.exception(e)
                print(e)
                pass
        if not get_success:
            all_url.remove(url)
        return False

    def fetch_url(self, content: str, current_url: str):
        url_list = list(set(re.findall(self.fetch_role, content)))
        base_current_url = current_url.split('?')[0]
        result_url = []
        for tem in url_list:
            tem_map = {'start_end': tem[1], 'origin_url': tem[2]}
            base_tem = tem[2].split('?')[0]
            # 如果 base_tem 为空不再请求
            if not base_tem:
                tem_map['request_url'] = base_current_url
                result_url.append(tem_map)
                continue
            if base_tem == '/':
                tem_map['request_url'] = self.base_url + base_tem
                result_url.append(tem_map)
                continue
            if (base_tem.startswith('https://') or base_tem.startswith('//') or base_tem.startswith('http://')) and \
                    self.host not in base_tem:
                continue
            if base_tem.startswith("http://"):
                base_tem = base_tem.replace("http:", "https")
            if base_tem.startswith("//"):
                base_tem = "https:" + base_tem
            if not base_tem.endswith('/') and '.' not in os.path.basename(base_tem):
                base_tem = base_tem + '/'
            if base_tem.startswith('https://' + self.host):
                tem_map['request_url'] = base_tem
            else:
                if base_tem in base_current_url:
                    tem_map['request_url'] = base_current_url
                    result_url.append(tem_map)
                    continue
                # 替换 #.*?/ 为 '/'
                fix_positions = re.findall('(#.*?)/', base_tem)
                for fix_position in fix_positions:
                    base_tem = base_tem.replace(fix_position, "#")
                if not base_tem or base_tem == '#/':
                    tem_map['request_url'] = base_current_url
                    result_url.append(tem_map)
                    continue
                base_tem = base_tem.replace("#", "")
                if base_tem.startswith('/'):
                    tem_map['request_url'] = self.base_url + base_tem
                else:
                    tem_map['request_url'] = base_current_url + base_tem
            if 'javascript' in tem_map['request_url'] or 'data:image' in tem_map['request_url']:
                tem_map['request_url'] = base_current_url
            if tem_map['request_url'].endswith('//'):
                tem_map['request_url'] = tem_map['request_url'][:-1]
            result_url.append(tem_map)
        return result_url

    def save_to_html(self, changed_url: list, url: str, content: str):
        file_name = self.transform_url_to_path(url)
        save_path = os.path.dirname(file_name)
        if not os.path.isdir(save_path):
            os.makedirs(save_path)
        path_level = len(file_name.split('/')) - 2
        path_add = ''
        for i in range(path_level):
            path_add += "../"
        for tem_url in changed_url:
            content = content.replace(tem_url['start_end'] + tem_url['origin_url'] + tem_url['start_end'],
                                      tem_url['start_end'] + path_add + self.transform_url_to_path(tem_url['request_url'])
                                      + tem_url['start_end'])
        with open(file_name, 'w', encoding='utf-8') as file_object:
            file_object.write(content)

    def transform_url_to_path(self, url: str):
        base_file_name = url.replace(self.base_url, './source')
        if base_file_name.endswith('/'):
            base_file_name = base_file_name[:-1] + '.html'
        elif base_file_name.endswith('.php'):
            base_file_name = base_file_name + '.html'
        return base_file_name


if __name__ == '__main__':
    start_spider = WebSpider('www.troublecodes.net')
    for net in ['https://www.troublecodes.net/pcodes/', 'https://www.troublecodes.net/bcodes/',
                'https://www.troublecodes.net/ccodes/', 'https://www.troublecodes.net/ucodes/']:
        Thread(target=start_spider.get_page, args=(net, )).start()
