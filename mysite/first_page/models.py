from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.
class Task(models.Model):
	name = models.CharField(max_length=50)
	deadline = models.DateField()
	price = models.IntegerField()
	user = models.CharField(max_length=50)

	def get_deadline(self):
		d = datetime.date.today()
		return (d-self.deadline)

	def __str__(self):
		return self.name