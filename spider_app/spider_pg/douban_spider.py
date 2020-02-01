# -*- coding: utf-8 -*-
"""爬取豆瓣top250,并且储存在本地的mysql数据库里"""

import requests
from lxml import etree
from spider_app.models import Test
from spider_app.spider_pg.factory import Factory


class DoubanSpider(Factory):
    """继承父类,工厂模式"""

    def __init__(self):
        self.respones_list = []
        self.n = 0
        self.rank = None
        self.name = None
        self.content = None
        self.date = None
        self.address = None
        self.data = None
        self.description = None
        self.star = None
        self.evaluation = None

    def get_data(self):
        html_list = [f'https://movie.douban.com/top250?start={num * 25}&filter=' for num in range(0, 10)]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome'
                          '/14.0.835.163 Safari/535.1'
        }
        for html in html_list:
            response = requests.get(html, headers=headers)
            self.respones_list.append(response.text)

    def parse_data(self):
        """
        把爬取下来的html源码转成可以用xpath解析的格式
        :return: 它会调用下面的save方法,直接存储到数据库
        """
        for respones in self.respones_list:
            item = etree.HTML(respones)
            l = item.xpath("//div[@class='article']//ol[@class='grid_view']/li")
            self.n += 1
            print(f"正在爬取第{self.n}页.")
            for i in l:
                self.rank = i.xpath(".//div[@class='item']//em/text()")[0]
                self.name = i.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()")[0]
                self.content = i.xpath(".//div[@class='bd']/p[1]/text()[2]")
                self.content = [''.join(ele) for ele in self.content[0].split("\xa0/\xa0")]
                # 日期
                self.date = self.content[0].split()[0]
                # 国家
                self.address = self.content[1].split()[-1]
                # print(self.address)
                # 星级
                self.star = i.xpath(".//span[@class='rating_num']/text()")[0]
                # 评论数
                self.evaluation = i.xpath(".//div[@class='star']/span[4]/text()")[0]
                # 描述
                self.description = i.xpath(".//p[@class='quote']/span/text()")[0]
                self.save_data()

    def save_data(self):

        """保存数据"""
        test1 = Test(
            rank=self.rank,
            name=self.name,
            star=self.star,
            num=self.evaluation,
            text=self.description,
            date=self.date,
            address=self.address,
        )
        test1.save()


if __name__ == '__main__':
    p1 = DoubanSpider()
    p1.process()
