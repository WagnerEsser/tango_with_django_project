# coding: utf-8
from django.shortcuts import redirect
from rango.forms import PageForm
from rango.views.category import *


def pages(request):
    page_list = Page.objects.order_by('-views')
    context_dict = {'pages': page_list}

    return render(request, 'rango/pages.html', context_dict)


@login_required
def add_page(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)  # cat está recebendo um objeto Category na qual se quer add a página
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                # probably better to use a redirect here.

                # return category(request, category_name_slug)
                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form':form, 'category': cat}

    return render(request, 'rango/add_page.html', context_dict)


def clique_numa_pagina(request):
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
            try:
                page = Page.objects.get(id=page_id)
                if page:
                    page.views = page.views+1;
                    page.save()
                    return redirect(page.url)
                else:
                    #return HttpResponse("Erro!")
                    return HttpResponse("Não Existe página!")
            except Page.DoesNotExist:
                return HttpResponse("Página não existe")
    return HttpResponseRedirect(reverse('rango:index'))