
from django.forms import ModelForm , PasswordInput, CharField
from django import forms
from django.contrib.auth import forms as f
from django.contrib.auth.models import User
from .models import Profile

# Create all user_handler form
class userForm(f.UserCreationForm):
	pass


class loginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(widget=PasswordInput())


# Create the update form
class UserUpdateForm(ModelForm):

	class Meta:
		model = User
		fields = ['username',]

class UserProfileUpdateForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['picture',]