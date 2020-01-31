# -*- coding: utf-8 -*-
# __author__ = 'GonzaloWang'
from spider.management.commands.douban_spider import DoubanSpider
from spider.management.commands import echarts2
import argparse
import re
import time
from spider.management.commands.test import outputcmd


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
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-s", help="输入douban来运行豆瓣爬虫", type=str)
#     # parser.add_argument("o", help="默认打印到控制台, 参数指定*.html")
#     parser.add_argument("-o", default='n', help="可选参数,输入*.html来生成报表,默认不生成报表.")
#     args = parser.parse_args()
#     # print("请输入python test.py ")
#     main(args.s, args.o)
