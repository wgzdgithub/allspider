# *_*coding:utf-8 *_*
# __author__ = 'GonzaloWang'
from django.core.management.base import BaseCommand

from spider_app.spider_pg import main


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
