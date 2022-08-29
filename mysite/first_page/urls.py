from django.urls import path
from . import views

app_name = 'first_page'
urlpatterns = [
    path('', views.show_page, name='show_page'),
    path('<int:page>', views.show_page, name='show_page_num'),
    path('info/<int:id>', views.info, name='info'),
    path('next<int:page>', views.next_page, name='next_page'),
    path('previous<int:page>', views.previous_page, name='previous_page'),
]
