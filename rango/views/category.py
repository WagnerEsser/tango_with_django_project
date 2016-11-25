# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from rango.models import Category, Page
from rango.forms import CategoryForm
from django.contrib.auth.decorators import login_required


def clique_numa_categoria(request):
    if request.method == 'GET':
        if 'category_id' in request.GET:
            category_id = request.GET['category_id']
            try:
                category = Category.objects.get(id=category_id)
                if category:
                    category.views = category.views+1
                    category.save()
                    return HttpResponseRedirect(reverse('rango:category', args=(category.slug,)))
                else:
                    return HttpResponse("Não Existe categoria!")
            except Category.DoesNotExist:
                return HttpResponse("Categoria não existe")
    return HttpResponseRedirect(reverse('rango:index'))


def categories(request):
    category_list = Category.objects.order_by('-likes')
    context_dict = {'categories': category_list}

    return render(request, 'rango/categories.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug) # .get retorna um objeto Category
        pages = Page.objects.filter(category=category) # .filter retorna um dicionário de objetos "Page"

        context_dict['category'] = category # passa o objeto Category
        context_dict['pages'] = pages # passa todas as páginas desse objeto em questão
    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context_dict)


@login_required
def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return HttpResponseRedirect(reverse('rango:index'))
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})


def curtir_uma_categoria(request):
    if request.method == 'GET':
        if 'category_id' in request.GET:
            category_id = request.GET['category_id']
            try:
                category = Category.objects.get(id=category_id)
                if category:
                    category.likes = category.likes+1;
                    category.save()
                    return HttpResponseRedirect(reverse('rango:category', args=(category.slug,)))
                else:
                    #return HttpResponse("Erro!")
                    return HttpResponse("Não Existe categoria!")
            except Category.DoesNotExist:
                return HttpResponse("Categoria não existe")
    return HttpResponseRedirect(reverse('rango:index'))