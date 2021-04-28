from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .form import userForm, loginForm, UserUpdateForm, UserProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import hashers as h
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.views.generic.list import ListView

# Create your views here.
def user_register(request):

	if request.method=="POST":
		register_form = userForm(request.POST)

		if register_form.is_valid():
			username = request.POST['username']
			password = request.POST['password1']
			try:
				# add user to database
				User.objects.create_user(username=username, email=None,password=password)
			except :
					# return to a form if any error accurs when we try to create the new user
					register_form = userForm(request.POST)
			else:
				# the new user can login with is password and username
				return redirect('login-to-home')

	else:
		register_form = userForm() 
	c = {'register_form': register_form}
	return render(request, 'register.html', c)

#==================================Logout view================================================
def user_logout(request):
	logout(request)
	return redirect("login-to-home")
#==================================Login view================================================
def user_login(request):
	login_form = loginForm()
	c = {'login_form' : login_form}
	if request.method == 'POST':
		login_form = loginForm(request.POST)

		if login_form.is_valid():
			# get the clean data from the submit form 
			username = request.POST['username'].strip()
			password = request.POST['password']
			# get all user matching
			try: 
				user = User.objects.get(username=username)
			except ObjectDoesNotExist:
				user = None;
			user_is_available = False # booleen for cheking password
			# check if the user exit $!
			if user is not None: 
				# for user in users:
					# check if the password match
				if h.check_password(password, user.password) :
					user_is_available = True
				if user_is_available: 
					# login seccussfull
					login(request, user)
					return redirect('user-profile')
				else:
					c['user_password_dn_match'] = "Username or password don't match.\n Please provide the right crendential"
					return render(request, 'login.html', c)
		

			else:
				c['user_dn_exist'] = "Username or password don't match. \nPlease provide the right credential!"
	return render(request, 'login.html', c)

#===========================User layout view================================================

def userProfile(request):
	if request.user.is_authenticated:
		allUserAvailable = User.objects.all()
		cont = {'allUserAvailable':allUserAvailable}
		return render(request, "all_profile.html", cont)
	else:
		return redirect('login-to-home')

#=======================User profile ===================
@login_required()
def users_settings(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form =UserProfileUpdateForm(request.POST, request.FILES , instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()

			messages.success(request, f"Your profile is successful update!")

			return redirect("user-profile")
	else :
		u_form = UserUpdateForm(instance=request.user)
		p_form =UserProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		 'p_form':p_form
		 }

	return render(request, "profile.html", context)











