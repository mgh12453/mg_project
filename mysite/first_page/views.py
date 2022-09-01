from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from .models import Task 
num_of_page = 0

def show_page(request, page=None):
    p = Paginator(Task.objects.all(), 5)

    if page != None:
        if p.num_pages < page:
            page = 1
        if page < 1:
            page = p.num_pages 
        request.session['page'] = page

    page = request.session.get('page', 1)
    context = {'page': page, 'num_page': p.num_pages, 'task': p.page(page).object_list}
    return render(request, 'first_page/index.html', context)

def info(request, id):
    task = Task.objects.get(pk=id)
    context = {'task': task}
    return render(request, 'first_page/info.html', context)
    
