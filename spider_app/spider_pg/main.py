# -*- coding: utf-8 -*-
# __author__ = 'GonzaloWang'
import re
import time
from spider_app.spider_pg import echarts2
from spider_app.spider_pg.douban_spider import DoubanSpider
from spider_app.spider_pg.test import outputcmd


def main1():
    """启动豆瓣爬虫and生成数据分析html"""
    p1 = DoubanSpider()
    start = time.perf_counter()
    p1.process()
    elapsed = time.perf_counter() - start
    print(f"爬取完成,耗时{elapsed}秒")


def main2(o):
    if re.match(".*?.html$", o):
        echarts2.mkhtml2(o)
        # echarts3.mkhtml3()
    else:
        print('参数错误')


def main3():
    outputcmd()


if __name__ == '__main__':
    main1()

