from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say(request, name=None):
    if(name == None):
        return HttpResponse('ooops\n you did not enter any name')
    return HttpResponse('SALAM {}'.format(name))
