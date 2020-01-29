# -*- coding: utf-8 -*-
"""爬取豆瓣top250,并且储存在本地的mysql数据库里"""
from factory import Factory
import requests
from lxml import etree
import mysql.connector
import yaml


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

        x = yaml.safe_load(open("config.yaml", 'r', encoding='utf-8').read())
        try:
            con = mysql.connector.connect(
                host=str(x['DB']['host']), port=str(x['DB']['port']),
                user=str(x['DB']['user']), password=str(x['DB']['password']),
                database=str(x['DB']['data'])
            )
            con.start_transaction()
            cursor = con.cursor()
            sql1 = "CREATE TABLE t_movies (排名 VARCHAR(200), " \
                   "名字 VARCHAR(200), 星级 VARCHAR(200), " \
                   "评论数 VARCHAR(200), 描述 VARCHAR(2000), 日期 VARCHAR (200), 地区 VARCHAR (200));"
            cursor.execute(sql1)
            con.commit()
        except Exception as e:
            con.rollback()
            print(e)

        finally:
            if 'con' in dir():
                con.close()

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
                self.data = f"{self.rank}", f"{self.name}", f"{self.star}", f"{self.evaluation}", f"{self.description}", f"{self.date}", f"{self.address}"
                self.save_data()

    def save_data(self):
        """保存数据"""
        x = yaml.safe_load(open("config.yaml", 'r', encoding='utf-8').read())
        try:
            con = mysql.connector.connect(
                host=str(x['DB']['host']), port=str(x['DB']['port']),
                user=str(x['DB']['user']), password=str(x['DB']['password']),
                database=str(x['DB']['data']),
            )
            con.start_transaction()
            cursor = con.cursor()
            sql2 = "INSERT INTO t_movies (排名, 名字, 星级, 评论数, 描述, 日期, 地区) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql2, (
                self.data[0], self.data[1], self.data[2], self.data[3], self.data[4], self.data[5], self.data[6]))
            con.commit()

        except Exception as e:
            con.rollback()
            print(e)

        finally:
            if 'con' in dir():
                con.close()
