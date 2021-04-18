	
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Message_m, Message_form, Message_In_box
# from django.db.models import Q
# from django.core import serializers
# import json

# Create your views here.

# =============avoid empty string or space caractere into database=========
def check_empty_string(strings):
	b = False
	if strings:
		for item in list(strings):
			if item==' ':
				b=False
			else:
				b=True
				break
	return b

#======================Chat with the user view==========================
def chatWithUser(request, username):
	if request.user.is_authenticated:
		if str(request.user.pk)<str(username):
			groupe_name = f'chat_{str(request.user.pk)}_{str(username)}'
		else:
			groupe_name = f'chat_{username}_{str(request.user.pk)}'
		
		all_message = Message_In_box.objects.filter(chat_room_message_name=groupe_name)

		username = User.objects.get(pk=username)
		username_id = username.pk
		myself = User.objects.filter(username=request.user)[0]
	
		return render(request,
			 'chat_app/chat_with_user.html',
			 context = {
				'myself'		: myself.username,
				'username'		: username.username,
				'all_message'	: all_message,
				'username_id'	: username_id 
				}
			)
	else:
		return redirect("login-to-home")










