#coding: utf-8
from django.db import models
from rango.models.question import QuestionModel


class ChoiceModel(models.Model):
    question = models.ForeignKey(QuestionModel)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def __unicode__(self):
        return self.choice_text