from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('<str:name>', views.say),
    path('', views.say),
]
