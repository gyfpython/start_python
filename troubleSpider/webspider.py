import os
import re

import requests
import multiprocessing

all_url = set()


class WebSpider(object):
    def __init__(self, host):
        global all_url
        self.base_url = 'https://' + host
        self.host = host
        self.fetch_role = '(https://' + host + '.*?)(\"|\')'
        self.current_dir = os.path.dirname(os.path.abspath(__file__))

    def login(self):
        pass

    def logout(self):
        pass

    def get_page(self, url: str):
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
        for i in range(5):
            try:
                response = requests.get(url=url, headers=headers, timeout=20)
                if url.endswith('.gif') or url.endswith('.png') or url.endswith('.jpg'):
                    file_name = self.transform_url(url)
                    if not os.path.isdir(os.path.dirname(file_name)):
                        os.makedirs(os.path.dirname(file_name))
                    with open(file_name, 'wb') as f:
                        f.write(response.content)
                    print('end spider {}'.format(url))
                    # all_url.add(url)
                    break
                changed_url = list(set(self.change_url(response.text)))
                self.save_to_html(changed_url, url, response.text)
                print('end spider {}'.format(url))
                # all_url.add(url)
                for url_tem in changed_url:
                    self.get_page(url_tem)
                break
            except Exception as e:
                print(e)
                pass
        return False

    def fetch_url(self, content: str):
        pass

    def change_url(self, content: str):
        url_list = re.findall(self.fetch_role, content)
        result_url = []
        for tem in url_list:
            result_url.append(tem[0])
        return result_url

    def save_to_html(self, changed_url: list, url: str, content: str):
        file_name = self.transform_url(url)
        if not os.path.isdir(os.path.dirname(file_name)):
            os.makedirs(os.path.dirname(file_name))
        for tem_url in changed_url:
            content = content.replace(tem_url + '\"', self.transform_url(tem_url) + '\"')
        with open(file_name, 'w', encoding='utf-8') as file_object:
            file_object.write(content)

    def transform_url1(self, url: str):
        base_file_name = url.replace(self.base_url, 'source').replace('/', '-')
        split_paras = base_file_name.split('?')
        url_split_paras = url.split('?')
        if '.' in url_split_paras[0].split('/')[-1]:
            if len(url_split_paras) <= 1:
                file_name = base_file_name
            else:
                split_point = split_paras[0].split('.')
                file_name = '.'.join(split_point[:-1]) + '_paras_' + split_paras[1] + '.' + split_point[-1]
        else:
            if len(split_paras) > 1:
                file_name = split_paras[0] + '_paras_' + split_paras[1] + '.html'
            else:
                file_name = split_paras[0] + '.html'
        return file_name

    def transform_url(self, url: str):
        base_file_name = url.replace(self.base_url, self.current_dir + '/source')
        split_paras = base_file_name.split('?')
        base_name = os.path.basename(split_paras[0])
        base_dir = os.path.dirname(split_paras[0])
        # print(base_dir)
        if base_name:
            if '.' in base_name:
                base_name_split = base_name.split('.')
                if len(split_paras) > 1:
                    file_path = base_dir + '/' + '.'.join(base_name_split[:-1]) + '_paras_' + split_paras[1] + '.' + \
                                base_name_split[-1]
                else:
                    file_path = split_paras[0]
            else:
                if len(split_paras) > 1:
                    file_path = base_dir + '/' + '_paras_' + split_paras[1] + '.html'
                else:
                    file_path = split_paras[0] + '.html'
        else:
            if len(split_paras) > 1:
                file_path = base_dir + '/' + 'index_paras_' + split_paras[1] + '.html'
            else:
                file_path = base_dir + '/' + 'index.html'
        return file_path


if __name__ == '__main__':
    start_spider = WebSpider('www.troublecodes.net')
    start_spider.get_page('https://www.troublecodes.net/')
    # pool = multiprocessing.Pool(processes=3)
    # for i in range(3):
    #     pool.map_async(start_spider.get_page, ('https://www.troublecodes.net/', ))
    # # start_spider.get_page('https://www.troublecodes.net/')
    # pool.close()
    # pool.join()
    # print('--------end------------------')