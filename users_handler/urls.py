
from django.urls import path
from . import views
import re


urlpatterns = [
	path('settings/', views.users_settings, name='users-settings'),
	path('', views.user_login, name='login-to-home'),
	path('login', views.user_login, name='login-to-home'),
	path('register', views.user_register, name='user-register'),
	path('logout', views.user_logout, name='logout-to-home'),
	path("profile/", views.userProfile, name='user-profile'),
]




