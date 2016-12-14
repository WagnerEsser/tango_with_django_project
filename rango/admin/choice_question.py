# coding: utf-8
from django.contrib import admin
from rango.models import *


class ChoiceInline(admin.TabularInline):
    model = ChoiceModel
    extra = 3


class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
    	(None, {'fields':['question']}),
        (None, {'fields': ['choice_text']}),
        (None, {'fields': ['votes']}),
    ]
    list_display = ('choice_text', 'votes', 'question')


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter  =  ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]


admin.site.register(QuestionModel, QuestionAdmin)
admin.site.register(ChoiceModel, ChoiceAdmin)