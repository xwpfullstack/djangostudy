from django.conf.urls import patterns, include, url
from fruit import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^people/(?P<personid>\d)/indent',
                           views.add_indent, name='add_indent'),
                       url(r'^choice_goods/$', views.choice_goods,
                           name='choice_goods'),
                       url(r'^goods_submit/$', views.goods_submit,
                           name='goods_submit'),
                       )
