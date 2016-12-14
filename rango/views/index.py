# coding: utf-8
from rango.models import CategoryModel, QuestionModel, PageModel
from django.shortcuts import render


def index(request):
    template = "rango/index.html"
    latest_question_list = QuestionModel.objects.order_by('-pub_date')[:5]
    category_list = CategoryModel.objects.order_by('-likes')[:5]
    page_list = PageModel.objects.order_by('-views')[:5]

    context_dict = {'categories': category_list, 'pages': page_list, 'latest_question_list': latest_question_list}

    return render(request, template, context_dict)