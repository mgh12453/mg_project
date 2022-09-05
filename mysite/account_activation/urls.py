from django.urls import path
from . import views

app_name = 'account_activation'
urlpatterns = [
    #path('send', views.send_email, name='send_email'),
    path('activate/<str:uidb64>/<str:token>', views.activate, name='activate')
]
