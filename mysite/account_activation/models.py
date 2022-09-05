from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class activation(models.Model):
	uid = models.IntegerField(default=1)
	token = models.CharField(max_length=200)