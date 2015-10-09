# coding=utf-8
from django.db import models
from datetime import datetime
# Create your models here.

# 店员


class Person(models.Model):
    name = models.CharField(max_length=16, verbose_name=u"店员姓名")

    def __unicode__(self):
        return self.name
# 物品类型


class Case(models.Model):
    name = models.CharField(max_length=16, verbose_name=u"物品类型")

    def __unicode__(self):
        return self.name
# 具体的物品


class Goods(models.Model):
    case = models.ForeignKey(Case)
    name = models.CharField(max_length=16, verbose_name=u"物品名称")
    price = models.IntegerField(default=0, verbose_name=u"物品单价")

    def __unicode__(self):
        return self.name
# 订单


class Indent(models.Model):
    person = models.ForeignKey(Person)
    goods = models.ForeignKey(Goods)
    count = models.IntegerField(default=1, verbose_name=u"物品数量")
    price = models.IntegerField(default=0, verbose_name=u"物品总价")
    time = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return str(self.id)