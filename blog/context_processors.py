#!/usr/bin/env python
# Author:ChenHuaJun
# -*- coding:utf-8 -*-

__author__ = 'JHao'

from blog.models import Category, Article, Tag


def sidebar(request):
    category_list = Category.objects.all()
    # 所有类型

    article_rank = Article.objects.all().order_by('-view')[0:6]
    # 文章排行

    tag_list = Tag.objects.all()
    # 标签

    return {
        'category_list': category_list,
        'article_rank': article_rank,
        'tag_list': tag_list,
    }


if __name__ == '__main__':
    pass
