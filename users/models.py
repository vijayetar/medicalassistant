from django.contrib.auth.models import AbstractUser
from django.db import models




class CustomUser(AbstractUser):
	email = models.EmailField(verbose_name = 'email', max_length = 160, unique=True)
	username = models.CharField(max_length=30, unique = True)
	date_joined = models.DateTimeField(verbose_name = 'date joined', auto_now_add = True)
	first_name = models.CharField(max_length = 64)
	last_name = models.CharField(max_length = 64)
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	
	def __str__(self):
		return self.username
