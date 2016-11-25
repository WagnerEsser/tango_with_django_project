# coding: utf-8
from rango.models import Category, Question, Page
from django.shortcuts import render


def index(request):
    template = "rango/index.html"
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {'categories': category_list, 'pages': page_list, 'latest_question_list': latest_question_list}

    return render(request, template, context_dict)