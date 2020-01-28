# *_*coding:utf-8 *_*
# __author__ = 'GonzaloWang'

from pyecharts.charts import Bar
from pyecharts import options as opts
import mysql.connector
import mysql


def mkhtml3():
    """
    柱状图
    :return:生成豆瓣top250电影评分分布html文件
    """
    con = mysql.connector.connect(
        host='localhost', port='3306',
        user='root', password='ww19971214',
        database='test',
    )
    sql = "SELECT 星级 AS '星级', COUNT(*) AS '统计量' FROM t_movies GROUP BY `星级`"  # sql查询语句
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
    bar.set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=10, interval=0)),
                        title_opts=opts.TitleOpts(title="电影评分分布", subtitle="电影数"))

    bar.add_xaxis(namelist)
    bar.add_yaxis("评分", numlist)
    # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
    # 也可以传入路径参数，如 bar.render("mycharts.html")
    bar.render("豆瓣top250电影评分分布.html")


if __name__ == '__main__':
    mkhtml3()
