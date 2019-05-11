#!/usr/bin/env python
# Author:ChenHuaJun
# -*- coding:utf-8 -*-

"""chj_blog_two URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include(('blog.urls', 'blog'), namespace='blog')),
    url(r'^blog/$', views.index, name='index'),
    url(r'^$', views.index),
    path('ueditor/', include('DjangoUeditor.urls')),  # 增加django_summernote映射
    path('resume/', views.resume, name='resume'),  # 简历路径
    path('weixin/', views.weixin, name='weixin'),  # 微信路径
    path('download/', views.download, name='download')  # 下载中心
]
