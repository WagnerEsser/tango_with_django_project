#coding: utf-8
from django.db import models
from rango.models.category import CategoryModel


class PageModel(models.Model):
    category = models.ForeignKey(CategoryModel)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title