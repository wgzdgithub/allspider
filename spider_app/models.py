from django.db import models


class Test(models.Model):
    rank = models.CharField("排名", max_length=20)
    name = models.CharField("电影名称", max_length=200)
    star = models.CharField("星级评分", max_length=200)
    num = models.CharField("评论数", max_length=200)
    text = models.CharField("描述", max_length=200)
    date = models.CharField("日期", max_length=200)
    address = models.CharField("发行国家", max_length=200)
# Create your models here.
