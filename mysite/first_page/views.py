from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Task 
num_of_page = 0

class page_error:
    signin_error_text = []
    signup_error_text = []

    def clear(self):
        self.signup_error_text.clear()
        self.signin_error_text.clear()

perror = page_error()

def show_page(request, page=None):
    p = Paginator(Task.objects.all(), 4)

    if page != None:
        if p.num_pages < page:
            page = 1
        if page < 1:
            page = p.num_pages 
        request.session['page'] = page

    page = request.session.get('page', 1)
    page_list = range(1, p.num_pages+1)
    context = {'page': page,
               'page_list': page_list, 
               'num_page': p.num_pages, 
               'task': p.page(page).object_list,
               'page_error': perror,
               'User': request.user,
               }
    ret = render(request, 'first_page/index.html', context)
    perror.clear()
    return ret

def info(request, id):
    task = Task.objects.get(pk=id)
    context = {'task': task}
    return render(request, 'first_page/details.html', context)

def signin(request):
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
    else:
        perror.signin_error_text.append('رمز عبور یا نام کاربری صحیح نمیباشد')
    return HttpResponseRedirect(reverse('first_page:show_page'))

def signup(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    password_rpt = request.POST.get('password_rpt')
    email = request.POST.get('email')
    is_master = request.POST.get('master')

    correct = True
    if not username or not password or not password_rpt or not email:
        correct = False
        perror.signup_error_text.append('فیلد های ضروری را پر کنید')
    if password != password_rpt:
        correct = False
        perror.signup_error_text.append('رمز عبور و تکرار رمز عبور یکسان نیست')
    if correct:
        user = User.objects.create_user(username=username, password=password, email=email)
        user.is_master = is_master
        user.is_active = True
        user.save()
        login(request, user)
    return HttpResponseRedirect(reverse('first_page:show_page'))
        
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_page:show_page'))
