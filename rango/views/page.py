# coding: utf-8
from django.shortcuts import redirect
from rango.forms import PageForm
from rango.views.category import *
from rango.models import CategoryModel, PageModel


class PageView(View):
    template = "rango/page.html"

    @method_decorator(login_required)
    def get(self, request, id=None, category_name_slug=None):
        if id:
            page = PageModel.objects.get(pk=id)
            category_name_slug = page.category.slug
            form = PageForm(instance=page)
        else:
            form = PageForm()
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id, 'category': category_name_slug})

    @method_decorator(login_required)
    def post(self, request, category_name_slug=None):
        try:
            cat = CategoryModel.objects.get(slug=category_name_slug)
        except CategoryModel.DoesNotExist:
            cat = None

        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            page = PageModel.objects.get(pk=id)
            form = PageForm(instance=page, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = PageForm(data=request.POST)

        if form.is_valid():
            page = form.save(commit=False)
            page.category = cat
            page.views = 0
            page.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id, 'category': category_name_slug})


@login_required
def PageDelete(request, id):
    page = PageModel.objects.get(pk=id)
    page.delete()
    return HttpResponseRedirect('/')


def Pages(request):
    page_list = PageModel.objects.order_by('-views')
    context_dict = {'pages': page_list}

    return render(request, 'rango/pages.html', context_dict)


def GoToPage(request):
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
            try:
                page = PageModel.objects.get(id=page_id)
                if page:
                    page.views += 1
                    page.save()
                    return redirect(page.url)
                else:
                    return HttpResponse("Não Existe página!")
            except PageModel.DoesNotExist:
                return HttpResponse("Página não existe")
    return HttpResponseRedirect(reverse('rango:index'))
