from django.shortcuts import render, redirect
from django.http import HttpResponse
import os

# Create your views here.
def search(request, query=None):
    # index = open('search/template/index.html', 'w')
    # index.write('<h1>You did not enter any word</h1>')
    # index.close()
    if(query == None):query = request.GET.get('Query', None)
    if(query == None):
        return HttpResponse('You did not enter any word')
    return redirect('https://www.google.com/search?channel=fs&client=ubuntu&q={}'.format(query))
