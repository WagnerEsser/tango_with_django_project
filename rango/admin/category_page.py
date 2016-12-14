# coding: utf-8
from django.contrib import admin
from rango.models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(PageModel)
admin.site.register(CategoryModel)