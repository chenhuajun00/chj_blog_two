#!/usr/bin/env python
# Author:ChenHuaJun
# -*- coding:utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.timezone import now
from DjangoUeditor.models import UEditorField


class Tag(models.Model):
    """标签模型：标签列表"""
    tag_name = models.CharField(verbose_name='标签名', max_length=30)
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    last_time = models.DateTimeField(verbose_name='修改时间', default=now)

    def __str__(self):
        """使对象后台显示更友好，显示自己输入的字段，而不是系统字段"""
        return self.tag_name

    class Meta:
        ordering = ['tag_name']
        verbose_name = '标签名称'  # 指定后台显示模型名称
        verbose_name_plural = '标签列表'  # 指定后台显示模型复数名称
        db_table = "tag"  # 数据库表名


class Category(models.Model):
    """类别模型：分类列表"""
    name = models.CharField(verbose_name='类别名称', max_length=30)
    created_time = models.DateTimeField(verbose_name='创建时间', default=now)
    last_mod_time = models.DateTimeField(verbose_name='修改时间', default=now)

    class Meta:
        ordering = ['name']
        verbose_name = "类别名称"
        verbose_name_plural = "分类列表"
        db_table = 'category'

    def __str__(self):
        return self.name


class Article(models.Model):
    """文章模型：文章列表"""
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )
    title = models.CharField(verbose_name='标题', max_length=70)  # 博客标题
    digest = models.TextField(verbose_name='摘要', max_length=300, blank=True, null=True)  # 文章摘要
    content = UEditorField('内容', width=1000, height=800, toolbars="full", imagePath="upimg/", filePath="upfile/",
                        upload_settings={"imageMaxSize": 1204000},
                        settings={}, command=None, blank=True
                        )  # 文章正文
    status = models.CharField(verbose_name='状态', max_length=1, choices=STATUS_CHOICES, default='p')
    category = models.ForeignKey(Category, verbose_name='文章类型', on_delete=models.CASCADE, blank=False, null=False)
    date_time = models.DateField(verbose_name='发布时间', default=now)  # 博客发布时间
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)
    view = models.BigIntegerField(verbose_name='浏览量', default=0)  # 阅读数
    tag = models.ManyToManyField(Tag, verbose_name='标签集合', blank=True)  # 标签

    def __str__(self):
        return self.title

    def viewed(self):
        """
        增加阅读数
        :return:
        """
        self.view += 1
        self.save(update_fields=['view'])

    class Meta:  # 按时间降序
        ordering = ['-date_time']
        verbose_name = '文章'
        verbose_name_plural = '文章列表'
        db_table = 'article'
