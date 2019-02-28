from selenium import webdriver
from flask import Flask
import json
import re
import lxml.html
etree = lxml.html.etree
import requests


class BaiduKwCrawler:

    def __init__(self, url):
        self.url = url

    def get_keyword_url(self):
        res = requests.get(self.url, verify=False)
        content = res.text
        pattern = re.compile(r'\((.*?)\)')
        json_text = re.findall(pattern, content, flags=0)[0]
        return json.loads(json_text)


# url = 'https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd={}&sugmode=2&json=1&p=3&sid=1434_21080_28557_28519_28415&bs=seo&pbs=seo&csor=3&pwd={}&cb=jQuery110202572147514217825_1551326474411&_=1551326474450'.format(
#         'seo', 'seo')
# crawler = BaiduKwCrawler(url)
# js = crawler.get_keyword_url()
# print(json.dumps(js, ensure_ascii=False))

app = Flask(__name__)


@app.route('/kw/<keyword>')
def return_kw(keyword):
    url = 'https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd={}&sugmode=2&json=1&p=3&sid=1434_21080_28557_28519_28415&bs=seo&pbs=seo&csor=3&pwd={}&cb=jQuery110202572147514217825_1551326474411&_=1551326474450'.format(
        keyword, keyword)
    crawler = BaiduKwCrawler(url)
    js = crawler.get_keyword_url()
    return json.dumps(js, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True)
