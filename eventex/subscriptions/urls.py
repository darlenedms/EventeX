# coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('eventex.subscriptions.views',
    url(r'^(\d+)/$', 'success', name='success'),
    url(r'^$', 'subscribe', name='subscribe'),
)
