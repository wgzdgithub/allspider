# *_*coding:utf-8 *_*
# __author__ = 'GonzaloWang'
from pyecharts.charts import Pie
from pyecharts import options as opts
from django.db.models import Count
from spider_app.models import Test


def mkhtml2(name1):
    """
    饼图
    :return:生成豆瓣top250电影产源国家数量占比分析图html文件
    """

    # ORM查询
    myresult = Test.objects.values('address').annotate(count=Count('name')).order_by('-count')[:10]
    # fetchall() 获取所有记录
    namelist = []
    # 将变量存在列表里
    numlist = []
    for name in myresult:
        namelist.append(name['address'])
        numlist.append(name['count'])

    pie = Pie()
    pie.add("占比",
            [list(z) for z in zip(namelist, numlist)],
            center=["40%", "60%"],
            )
    pie.set_global_opts(
        title_opts=opts.TitleOpts(title="豆瓣top250电影产源国家数量占比"),
        legend_opts=opts.LegendOpts(pos_left="35%"),
    )
    # 设置显示的样子，加入了百分比
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))
    pie.render(f'{name1}')
    print(f'{name1}已生成')


if __name__ == '__main__':
    mkhtml2("自定义名字")
