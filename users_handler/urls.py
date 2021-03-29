
from django.urls import path
from . import views
import re


urlpatterns = [
	path('', views.user_register, name='user-register'),
	path('login', views.user_login, name='login-to-home'),
	path('logout', views.user_logout, name='logout-to-home'),
	path("profile/", views.userProfile, name='user-profile'),
]




