import datetime
from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Task(models.Model):
	user = models.OneToOneField(User, default=None, on_delete=models.SET_DEFAULT)
	name = models.CharField(max_length=50)
	price = models.IntegerField()
	deadline = models.DateField()
	details = models.TextField(default='کارگذار هیچ توضیحی برای این کار اضافه نکرده است')

	def get_deadline(self):
		d = datetime.date.today()
		return (d-self.deadline).days

	def __str__(self):
		return self.name

class FormTask(ModelForm):
	class Meta:
		model = Task
		fields = ['name', 'price', 'deadline', 'details']


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

