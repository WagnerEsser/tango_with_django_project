#coding: utf-8
import datetime
from django.db import models
from django.utils import timezone


class QuestionModel(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Publicado recentemente?'

    def __str__(self):
        return self.question_text

    def __unicode__(self):
        return self.question_text