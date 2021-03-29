"""
ASGI config for chat_room project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import django
django.setup()


import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter , URLRouter
from channels.auth import AuthMiddlewareStack
import chat_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_room.settings')

application = ProtocolTypeRouter({
	'http': get_asgi_application(),
	'websocket': AuthMiddlewareStack(
		URLRouter(
			chat_app.routing.websocket_urlpatterns
			)
		),
	})
