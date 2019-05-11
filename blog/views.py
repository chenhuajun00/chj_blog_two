#!/usr/bin/env python
# Author:ChenHuaJun
# -*- coding:utf-8 -*-

from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category


def index(request):
    """
    博客首页
    :param request:
    :return:
    """
    article_list = Article.objects.all().order_by('-date_time')[0:5]
    return render(request, 'blog/index.html', {"article_list": article_list, "source_id": "index"})


def articles(request, pk):
    """
    博客列表页面
    :param request:
    :param pk:
    :return:
    """
    pk = int(pk)
    if pk:
        category_object = get_object_or_404(Category, pk=pk)
        category = category_object.name
        article_list = Article.objects.filter(category_id=pk)
    else:
        # pk为0时表示全部
        article_list = Article.objects.all()  # 获取全部文章
        category = u''
    return render(request, 'blog/articles.html', {"article_list": article_list, "category": category, })


def about(request):
    return render(request, 'blog/about.html')


def archive(request):
    article_list = Article.objects.order_by('-date_time')
    return render(request, 'blog/archive.html', {"article_list": article_list})


def link(request):
    return render(request, 'blog/link.html')


def message(request):
    return render(request, 'blog/message_board.html', {"source_id": "message"})


def detail(request, pk):
    """
    博文详情
    :param request:
    :param pk:
    :return:
    """
    article = get_object_or_404(Article, pk=pk)
    article.viewed()
    return render(request, 'blog/detail.html', {"article": article,
                                                "source_id": article.id})


def search(request):
    """
    搜索
    :param request:
    :return:
    """
    key = request.GET['key']
    article_list = Article.objects.filter(title__icontains=key)
    return render(request, 'blog/search.html', {"article_list": article_list, "key": key})


def tag(request, name):
    """
    标签
    :param request:
    :param name
    :return:
    """
    article_list = Article.objects.filter(tag__tag_name=name)
    return render(request, 'blog/tag.html', {"article_list": article_list, "tag": name})


def resume(request):
    """跳转简历"""
    return render(request, 'resume.html')


def weixin(request):
    """跳转微信"""
    return render(request, 'weixin.html')


def download(request):
    """跳转下载中心"""
    return render(request, 'download.html')
