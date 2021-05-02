from django.db import models
from django.forms import ModelForm , PasswordInput, CharField
from django import forms
from django.contrib.auth import forms as f
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

	

#User profile
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	picture = models.ImageField(default='user.jpeg', upload_to='profile_image')

	def __str__(self):
		return f'{self.user.username} profile'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		ima = Image.open(self.picture.path)

		if ima.height>300 or ima.width>300:
			new_size = (200, 200)
			ima.thumbnail(new_size)
			ima.save(self.picture.path)

