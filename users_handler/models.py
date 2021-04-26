from django.db import models
from django.forms import ModelForm , PasswordInput, CharField
from django import forms
from django.contrib.auth import forms as f
from django.contrib.auth.models import User
# from djam


# Create your models here.
class userForm(f.UserCreationForm):
	pass

class loginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(widget=PasswordInput())
	
#User profile (images)
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	picture = models.ImageField(default='user.jpeg', upload_to='profile_image')

	def __str__(self):
		return f'{self.user.username} profile'
