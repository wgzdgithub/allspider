# -*- coding: utf-8 -*-
from douban_spider import Douban_spider
import echarts2
import echarts3
import click


# def main():
#     a = input("请输入豆瓣")
#     if a == '豆瓣':
#         p1 = Douban_spider()
#         p1.process()
#     b = input("请输入1生成数据可视化html")
#     if b == '1':
#         echarts2.mkhtml2()
@click.command()
@click.option('-s', required=True, type=click.Choice(['douban', 'tieba']),
              help='start spider, please input douban or tieba.')
@click.option('-h', required=True, type=click.Choice(['y', 'n']), prompt='Generate data analysis page',
              help='The person to greet.')
def main(s, h):
    """启动豆瓣爬虫and生成数据分析html"""
    if s == 'douban':
        p1 = Douban_spider()
        p1.process()
    else:
        pass
    if h == 'y':
        echarts2.mkhtml2()
        echarts3.mkhtml3()
    else:
        pass


if __name__ == '__main__':
    main()
