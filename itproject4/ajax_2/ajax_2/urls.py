from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ajax_2.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^$', 'ajax.views.index', name='home'),
                       url(r'^add/$', 'ajax.views.add', name='add'),
                       url(r'^ajax_list/$', 'ajax.views.ajax_list',
                           name='ajax-list'),
                       url(r'^ajax_dict/$', 'ajax.views.ajax_dict',
                           name='ajax-dict'),

                       )
