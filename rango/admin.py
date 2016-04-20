from django.contrib import admin
from rango.models import Category, Page, Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
    	(None,				 {'fields':['question']}),
        (None,               {'fields': ['choice_text']}),
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

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Page)
admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)