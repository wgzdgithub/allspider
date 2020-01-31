# *_*coding:utf-8 *_*
# __author__ = 'GonzaloWang'
from django.core.management.base import BaseCommand

from TestModel import main


class Command(BaseCommand):
    help = """
        练习自定义django命令行
    """

    def add_arguments(self, parser):
        """
        添加两个命令行参数
        1.爬虫开始 --start
        2.生成报表 --mkhtml
        :param parser:
        :return:
        """
        parser.add_argument(
            "-s",
            type=str,
            dest='spider',
            action='store',
            help="加参数'douban'开始爬取",
        )

        parser.add_argument(
            '-o',
            dest="output",
            action='store',
            default=False,
            help='加参数*.html生成报表',
        )

    def handle(self, *args, **options):
        # self.stdout.write(options['square'])
        if options['spider'] == 'douban':
            if options['spider'] == 'douban':
                main.main1()
            if options['output']:
                main.main2(options['output'])
            else:
                main.main3()
        elif options['spider'] != 'douban':
            self.stdout.write('参数错误')

    # def main(self, s, o):
    #     print(s)
    #     print(o)
    #     """启动豆瓣爬虫and生成数据分析html"""
    #     if s == 'douban':
    #         p1 = DoubanSpider()
    #         start = time.perf_counter()
    #         p1.process()
    #         elapsed = time.perf_counter() - start
    #         print(f"爬取完成,耗时{elapsed}秒")
    #     if re.match(".*?.html$", o):
    #         echarts2.mkhtml2(o)
    #         # echarts3.mkhtml3()
    #     if o == 'n':
    #         outputcmd()
