# -*- coding: utf-8 -*-
# __author__ = 'GonzaloWang'
from douban_spider import Douban_spider
import echarts2
import argparse
import re
import time


def main():
    """启动豆瓣爬虫and生成数据分析html"""
    if args.s == 'douban':
        p1 = Douban_spider()
        start = time.perf_counter()
        p1.process()
        elapsed = time.perf_counter() - start
        print(f"爬取完成,耗时{elapsed}秒")
    else:
        pass
    if re.match(".*?.html$", args.o):
        echarts2.mkhtml2(args.o)
        # echarts3.mkhtml3()
    else:
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--s", "-s", help="输入douban来运行豆瓣爬虫", type=str)
    # parser.add_argument("o", help="默认打印到控制台, 参数指定*.html")
    parser.add_argument("--o", "-o", default='n', help="可选参数,输入*.html来生成报表,默认不生成报表.")
    args = parser.parse_args()
    # print("请输入python test.py ")
    main()
