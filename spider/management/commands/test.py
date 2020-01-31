# *_*coding:utf-8 *_*
# __author__ = 'GonzaloWang'
import yaml
import mysql.connector
import os




def outputcmd():
    """
    输出到命令行统计信息
    :return: 命令行统计信息
    """
    with open("config.yaml", 'r', encoding='utf-8')as f:
        x = yaml.safe_load(f)

    con = mysql.connector.connect(
        host=str(x['DB']['host']), port=str(x['DB']['port']),
        user=str(x['DB']['user']), password=str(x['DB']['password']),
        database=str(x['DB']['data']),
    )
    sql = "SELECT 地区 AS '地区', COUNT(*) AS '统计量' FROM t_movies GROUP BY `地区` ORDER BY 统计量 DESC LIMIT 0, 10"  # sql查询语句
    mycursor = con.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    namelist = []
    numlist = []
    for name in myresult:
        namelist.append(name[0])
        numlist.append(name[1])
    print("豆瓣top250电影产源国家数量统计如下:")
    print('')
    print('')
    print(namelist[0] + "   " + "=" * numlist[0] + "---" + str(numlist[0]) + "部" + "占比" + str(numlist[0] / 2.5) + "%")
    print(namelist[1] + "   " + "=" * numlist[1] + "---" + str(numlist[1]) + "部" + "占比" + str(numlist[1] / 2.5) + "%")
    print(namelist[2] + "=" * numlist[2] + "---" + str(numlist[2]) + "部" + "占比" + str(numlist[2] / 2.5) + "%")
    print(namelist[3] + "   " + "=" * numlist[3] + "---" + str(numlist[3]) + "部" + "占比" + str(numlist[3] / 2.5) + "%")
    print(namelist[4] + "   " + "=" * numlist[4] + "---" + str(numlist[4]) + "部" + "占比" + str(numlist[4] / 2.5) + "%")
    print(namelist[5] + "   " + "=" * numlist[5] + "---" + str(numlist[5]) + "部" + "占比" + str(numlist[5] / 2.5) + "%")
    print(namelist[6] + "=" * numlist[6] + "---" + str(numlist[6]) + "部" + "占比" + str(numlist[6] / 2.5) + "%")
    print(namelist[7] + "   " + "=" * numlist[7] + "---" + str(numlist[7]) + "部" + "占比" + str(numlist[7] / 2.5) + "%")
    print(namelist[8] + " " + "=" * numlist[8] + "---" + str(numlist[8]) + "部" + "占比" + str(numlist[8] / 2.5) + "%")
    print(namelist[9] + " " + "=" * numlist[9] + "---" + str(numlist[9]) + "部" + "占比" + str(numlist[9] / 2.5) + "%")
