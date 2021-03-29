from django.db import models
from django.forms import  ModelForm, Textarea
from django.contrib.auth.models import User
from django import forms
import time

		
class Message_m(models.Model):
	my_message = models.TextField()
	time_message= models.DateTimeField(auto_now=time.time(), null=True)
	author = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

	class Meta:
		ordering = ['time_message']

	def __str__(self):
		return f'{self.author}'
	
class Message_In_box(models.Model):
	message = models.TextField()
	time_message= models.DateTimeField(auto_now=time.time(), null=True)
	author = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
	chat_room_message_name = models.CharField(max_length=30)
	class Meta:
		pass
	def __str__(self):
		return self.chat_room_message_name

class Message_form(forms.Form):
	my_messages = forms.CharField(initial='', widget=forms.Textarea, required=False)

	class Meta:
		pass

