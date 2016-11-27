#coding: utf-8
from django.db import models
from rango.models.category import Category


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0) # contabilizando

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title