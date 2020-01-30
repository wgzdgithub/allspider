# *_*coding:utf-8 *_*
# __author__ = 'GonzaloWang'
from django.core.management.base import BaseCommand


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
            '--start',
            action='store',
            dest='start',
            default=False,
            help='爬虫开始'
        )

        parser.add_argument(
            '--mkhtml',
            action='store',
            dest='mkhtml',
            default=False,
            help='生成报表'
        )

    def handle(self, *args, **options):
        if options['start']:
            self.stdout.write("开始爬取")
            self.stdout.write("-------")
            self.stdout.write("爬取结束")
        elif options['mkhtml']:
            self.stdout.write("开始生成")
            self.stdout.write("-------")
            self.stdout.write("已生成报表")
        else:
            self.stderr.write("指令错误")


