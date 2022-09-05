from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse
from .models import activation

# Create your views here.

def send_activation_mail(request, user):
	token_generator = PasswordResetTokenGenerator()
	acc = activation(uid=user.pk, token=token_generator.make_token(user))
	acc.save()
	uid = urlsafe_base64_encode(force_bytes(user.pk))
	context = {'domain': request.get_host(),'uidb64': uid, 'token': acc.token}

	subject = "Activation link"
	message = render_to_string('account_activation/activation_email.html', context)
	send_mail(subject, message, 'sender12453@yahoo.com', [user.email])

def activate(request, uidb64, token):
	uid = force_str(urlsafe_base64_decode(uidb64))
	user = User.objects.get(pk=uid)
	acc = activation.objects.get(uid=uid)

	if user is not None and acc.token == token:
		user.is_active = True;
		user.save()
		login(request, user)
		return HttpResponseRedirect(reverse('first_page:show_page'))
	else:
		return HttpResponse('<h1 style="text-align: center; color: tomato;">فعال سازی اکانت با خطا مواجه شد</h1>')
