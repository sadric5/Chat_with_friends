from django.urls import path
from . import views
import re

urlpatterns = [
    path(r'<str:username>', views.chatWithUser, name='chatUsers'), 	
]