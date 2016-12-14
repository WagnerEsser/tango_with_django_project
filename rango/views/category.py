# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from rango.models import CategoryModel, PageModel
from rango.forms import CategoryForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import View


class CategoryView(View):
    template = "rango/category.html"

    @method_decorator(login_required)
    def get(self, request, id=None):
        if id:
            category = CategoryModel.objects.get(pk=id)
            form = CategoryForm(instance=category)
        else:
            form = CategoryForm()
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    @method_decorator(login_required)
    def post(self, request):
        if request.POST['id']:
            id = request.POST['id']
            category = CategoryModel.objects.get(pk=id)
            form = CategoryForm(instance=category, data=request.POST)
        else:
            id = None
            form = CategoryForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('rango:index'))
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


@login_required
def CategoryDelete(request, id):
    category = CategoryModel.objects.get(pk=id)
    category.delete()
    return HttpResponseRedirect('/')


def ListCategories(request):
    category_list = CategoryModel.objects.order_by('-likes')
    context_dict = {'categories': category_list}
    return render(request, 'rango/categories.html', context_dict)


def ShowCategory(request, category_name_slug):
    context_dict = {}
    try:
        category = CategoryModel.objects.get(slug=category_name_slug)
        pages = PageModel.objects.filter(category=category)

        context_dict['category'] = category
        context_dict['pages'] = pages
    except CategoryModel.DoesNotExist:
        pass
    return render(request, 'rango/category-show.html', context_dict)


def GoToCategory(request):
    if request.method == 'GET':
        if 'category_id' in request.GET:
            category_id = request.GET['category_id']
            try:
                category = CategoryModel.objects.get(id=category_id)
                if category:
                    category.views += 1
                    category.save()
                    return HttpResponseRedirect(reverse('rango:category', args=(category.slug,)))
                else:
                    return HttpResponse("Não Existe categoria!")
            except CategoryModel.DoesNotExist:
                return HttpResponse("Categoria não existe")
    return HttpResponseRedirect(reverse('rango:index'))


def LikeCategory(request):
    if request.method == 'GET':
        if 'category_id' in request.GET:
            category_id = request.GET['category_id']
            try:
                category = CategoryModel.objects.get(id=category_id)
                if category:
                    category.likes += 1
                    category.save()
                    return HttpResponseRedirect(reverse('rango:category', args=(category.slug,)))
                else:
                    return HttpResponse("Não Existe categoria!")
            except CategoryModel.DoesNotExist:
                return HttpResponse("Categoria não existe")
    return HttpResponseRedirect(reverse('rango:index'))
