from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from .models import Task 

def show_page(request, page=1):
    try:
        p = Paginator(Task.objects.all(), 5)
        context = {'page': page, 'task': p.page(page).object_list}
        return render(request, 'first_page/index.html', context)
    except:
        return None

def info(request, id):
    task = Task.objects.get(pk=id)
    context = {'task': task}
    return render(request, 'first_page/info.html', context)
    

def next_page(request, page):
    show = show_page(request, page+1)
    if show == None:
        return show_page(request, 1)
    return show

def previous_page(request, page):
    show = show_page(request, page-1)
    if show == None:
        return show_page(request, int(Task.objects.count()/5))
    return show
