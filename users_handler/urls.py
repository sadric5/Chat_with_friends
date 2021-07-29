
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
import re


urlpatterns = [
	path('settings/', views.users_settings, name='users-settings'),
	path('', views.user_login, name='login-to-home'),
	path('login2', LoginView.as_view(template_name='login_page.html'), name='login-to-home'),
	path('login', views.user_login, name='login-to-home'),
	path('register', views.user_register, name='user-register'),
	path('logout', views.user_logout, name='logout-to-home'),
	path("profile/", views.userProfile, name='user-profile'),
]




