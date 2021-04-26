from django.apps import AppConfig


class UsersHandlerConfig(AppConfig):
    name = 'users_handler'
	def ready(self):
		import users_handler.signals
