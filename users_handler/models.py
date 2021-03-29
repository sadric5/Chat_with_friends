from django.db import models
from django.forms import ModelForm , PasswordInput, CharField
from django import forms
from django.contrib.auth import forms as f
# from djam


# Create your models here.
class userForm(f.UserCreationForm):
	pass

class loginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(widget=PasswordInput())
	



	# class Meta:
	# 	model = userformData
	# 	fields = "__all__"
	# 	# fields = ('username', 'password')

	# 	widgets = {
	# 		# 'username' : CharField(max_length=30),
	# 		'password' : PasswordInput()
	# 	 }

	# 	error_messages = {
	# 		'password' : {
	# 			"max_length" : ("Your password don't match. Please enter your correct password")
	# 		},
			 

	# 	}
