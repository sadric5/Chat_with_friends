from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Message_m, Message_form, Message_In_box
from django.db.models import Q
from django.core import serializers
import json



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

# def chat_display(request):
# 	all_message = Message_m.objects.all() 
# 	my_form =Message_form(None)
# 	if request.method=='POST':
# 		my_form = Message_form(request.POST)
# 		if my_form.is_valid():
# 			message = request.POST['my_messages']
# 			if check_empty_string(message):
# 				Message_m.objects.create(my_message=message, author=request.user)
# 				my_form = Message_form(None)					
# 	else:
# 		my_form =Message_form(None)
# 	cont={'all_message':all_message, 'message_form':my_form}
# 	return render(request, 'chat_app/chat.html', cont)

#======================Chat with the user view==========================
def chatWithUser(request, username):
	if request.user.is_authenticated:
		if str(request.user)<str(username):
			groupe_name = f'chat_{str(request.user)}_{str(username)}'
		else:
			groupe_name = f'chat_{username}_{str(request.user)}'
		# all_message = Message_In_box.objects.all()
		all_message = Message_In_box.objects.filter(chat_room_message_name=groupe_name)

		username = User.objects.filter(username=username)[0]
		myself = User.objects.filter(username=request.user)[0]
		print(type(request.user))

		return render(request,
			 'chat_app/chat_with_user.html',
			 context = {
				'myself':str(myself),
				'username':str(username),
				'all_message':all_message, 
				}
			)
	else:
		return redirect("login-to-home")










