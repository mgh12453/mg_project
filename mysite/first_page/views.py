from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from .models import Task 
num_of_page = 0

def show_page(request, page=None):
    p = Paginator(Task.objects.all(), 4)

    if page != None:
        if p.num_pages < page:
            page = 1
        if page < 1:
            page = p.num_pages 
        request.session['page'] = page

    page = request.session.get('page', 1)
    page_list = range(1, p.num_pages+1)
    context = {'page': page, 'page_list': page_list, 'num_page': p.num_pages, 'task': p.page(page).object_list}
    return render(request, 'first_page/index.html', context)

def info(request, id):
    task = Task.objects.get(pk=id)
    context = {'task': task}
    return render(request, 'first_page/details.html', context)
    
