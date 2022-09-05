from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Task
from account_activation.views import send_activation_mail

class page_error:
    signin_error_text = []
    signup_error_text = []
    signup_succes_text = []

    def clear(self):
        self.signup_error_text.clear()
        self.signin_error_text.clear()
        self.signup_succes_text.clear()

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
    context = {
            'page': page,
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
    if user is not None and user.is_active:
        login(request, user)
    if not user.is_active:
        perror.signin_error_text.append('اکانت وارد شده فعال نشده است. برای فعال سازی به ایمیل خود مراجعه کنید')
    if user is None:
        perror.signin_error_text.append('رمز عبور یا نام کاربری صحیح نمیباشد')
    return HttpResponseRedirect(reverse('first_page:show_page'))

def signup(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    password_rpt = request.POST.get('password_rpt')
    email = request.POST.get('email')
    if request.POST.get('master')=='on':
        is_master = True
    else:
        is_master = False
    correct = True
    if not username or not password or not password_rpt or not email:
        correct = False
        perror.signup_error_text.append('فیلد های ضروری را پر کنید')
    if password != password_rpt:
        correct = False
        perror.signup_error_text.append('رمز عبور و تکرار رمز عبور یکسان نیست')
    if User.objects.filter(username=username).count() > 0:
        correct = False
        perror.signup_error_text.append('نام کاربری وارد شده قبلا استفاده شده است')   
    if correct:
        user = User.objects.create_user(username=username, password=password, email=email)
        # user.master = master(user=user, is_master=is_master)
        user.profile.is_master = is_master
        user.is_active = False
        user.save()
        send_activation_mail(request, user)
        perror.signup_succes_text.append('ثبت نام شما با موفقیت اناجم شد. لطفا ایمیل خود را تایید کنید.')
    return HttpResponseRedirect(reverse('first_page:show_page'))
        
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_page:show_page'))
