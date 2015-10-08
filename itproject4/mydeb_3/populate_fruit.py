# coding=utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mydeb.settings')

import django
django.setup()

from fruit.models import *


def add_person(name):
    c = Person.objects.get_or_create(name=name)[0]
    return c


def add_case(name):
    c = Case.objects.get_or_create(name=name)[0]
    return c


def add_goods(case, name, price):
    c = Goods.objects.get_or_create(case=case, name=name, price=price)
    return c


def populate():
    add_person(name='小红')
    add_person(name='小丽')
    add_person(name='阿妹')

    fruit_case = add_case(name='水果')
    add_goods(case=fruit_case, name='苹果', price=10)
    add_goods(case=fruit_case, name='香蕉', price=20)
    add_goods(case=fruit_case, name='橘子', price=30)
    add_goods(case=fruit_case, name='火龙果', price=50)

    vega_case = add_case(name='蔬菜')
    add_goods(case=vega_case, name='黄瓜', price=5)
    add_goods(case=vega_case, name='西红柿', price=8)
    add_goods(case=vega_case, name='生菜', price=2)

    snack_case = add_case(name='零食')
    add_goods(case=snack_case, name='士力架', price=4)
    add_goods(case=snack_case, name='老婆饼', price=10)
    add_goods(case=snack_case, name='蛋挞', price=12)

if __name__ == '__main__':
    print "Starting fruit population script..."
    populate()
