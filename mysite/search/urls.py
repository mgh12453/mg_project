from django.urls import path
from . import views

urlpatterns = [
    path('', views.search),
    path('<str:query>', views.search),
]
