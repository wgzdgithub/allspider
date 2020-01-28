# *_*coding:utf-8 *_*
# __author__ = 'GonzaloWang'
from pyecharts.charts import Bar, Pie
from pyecharts import options as opts
import mysql.connector
import mysql


def mkhtml2(name1):
    """
    饼图
    :return:生成豆瓣top250电影产源国家数量占比分析图html文件
    """
    con = mysql.connector.connect(
        host='localhost', port='3306',
        user='root', password='ww19971214',
        database='test',
    )
    sql = "SELECT 地区 AS '地区', COUNT(*) AS '统计量' FROM t_movies GROUP BY `地区` ORDER BY 统计量 DESC LIMIT 0, 10"  # sql查询语句
    mycursor = con.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()  # fetchall() 获取所有记录
    """
    将变量存在列表里
    """
    namelist = []
    numlist = []
    for name in myresult:
        namelist.append(name[0])
        numlist.append(name[1])
    # print(len(namelist))
    # print(numlist)
    bar = Bar()
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
    mkhtml2()
