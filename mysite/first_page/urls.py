from django.urls import path
from . import views

app_name = 'first_page'
urlpatterns = [
    path('', views.show_page, name='show_page'),
    path('<int:page>', views.show_page, name='show_page'),
    path('info/<int:id>', views.info, name='info'),
]
