import datetime
from django.db import models
from django.utils import timezone
from django.forms import ModelForm, ValidationError
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Task(models.Model): 
	user = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_DEFAULT)
	name = models.CharField(max_length=50)
	owner =	models.CharField(default=None, null=True, max_length=50)
	price = models.IntegerField()
	deadline = models.DateField()
	details = models.TextField(default='کارگذار هیچ توضیحی برای این کار اضافه نکرده است')

	def get_deadline(self):
		d = datetime.date.today()
		return (self.deadline-d).days

	def __str__(self):
		return self.name

class FormTask(ModelForm):
	class Meta:
		model = Task
		fields = ['name', 'price', 'deadline', 'details']
		labels = {
			'name': 'عنوان',
			'price': 'قیمت',
			'deadline': 'توضیحات',
			'details': 'زمان تخمینی',
		}
		error_messages = {
			'name': {'invalid':'مقدار وارد شده نامعتبر است', 'required':'پر کردن این فیلد اجباری است'},
			'price': {'invalid':'مقدار وارد شده نامعتبر است', 'required':'پر کردن این فیلد اجباری است'},
			'deadline': {'invalid':'مقدار وارد شده نامعتبر است', 'required':'پر کردن این فیلد اجباری است'},
			'details': {'invalid':'مقدار وارد شده نامعتبر است', 'required':'پر کردن این فیلد اجباری است'},
		}

	def clean_price(self):
		super().clean()
		price = self.cleaned_data['price']
		if price < 1000 or price > 50000:
			raise ValidationError('قیمت باید عددی بین ۱۰۰۰ تا ۵۰۰۰۰ باشد')
		return price

	def clean(self):
		super().clean()
		price = self.cleaned_data.get('price', None)
		date = self.cleaned_data.get('deadline', None)
		if not date or not price:
			return

		d = datetime.date.today()
		if (date-d).days <= 3 and price > 30000:
			raise ValidationError('حداکثر قیمت کار‌های با زمان ۳ روز ۳۰۰۰۰ تومان می باشد')

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	is_master = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

