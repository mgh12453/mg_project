from django.urls import path
from . import views

app_name = 'first_page'
urlpatterns = [
    path('', views.show_page, name='show_page'),
    path('<int:page>', views.show_page, name='show_page'),
    path('load_more/<int:page>', views.load_more, name='load_more'),
    path('must_login', views.must_login, name='must_login'),
    path('info/', views.info, name='info'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('new_task', views.new_task, name='new_task'),
    path('assign_task/<int:tid>', views.assign_task, name='assign_task'),
]
