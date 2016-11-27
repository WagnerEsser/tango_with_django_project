#coding: utf-8
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0) # contabilizando
    likes = models.IntegerField(default=0) # contabilizando
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        # if self.id is None:
             # self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    # a função __unicode__ habilita retornar uma string na nossa codificação UTF-8, no campo 'name'
    def __unicode__(self):
        return self.name