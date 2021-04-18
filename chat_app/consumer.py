from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from .models import Message_In_box, Message_m
import datetime



class ChatConsumer(WebsocketConsumer):

	#accept all incomming connection 
	def connect(self):
		# get a chat room name
		self.chat_name = self.scope['url_route']['kwargs']['chat_name']
		#create a groupe name
		self.username = self.scope['user'].pk
		self.chatName = self.chat_name.rstrip('/')	#remove trailling slash
		
		if str(self.chatName)<str(self.username):
			self.chat_groupe_name = f'chat_{self.chatName}_{self.username}'
		else:
			self.chat_groupe_name = f'chat_{self.username}_{self.chatName}'

		# add all incoming connection with a goupe name to a groupe
		async_to_sync(self.channel_layer.group_add)(
			self.chat_groupe_name,
			self.channel_name
			)

		self.accept()

	
	# populate the message receive by the websocket to everyone in the chat groupe "self.chat_groupe-name"
	def receive(self, text_data):
		tex_data_json = json.loads(text_data)
		message = tex_data_json['message']
		user = tex_data_json['user']
		time = tex_data_json['time']

		#Call the storing function to store all data to a database
		self.create_chat_message(message, self.chat_groupe_name)
		# send the message to the groupe
		async_to_sync(self.channel_layer.group_send)(
			self.chat_groupe_name,
			{
				'type': 'chat_message',
				'message': message,
				'user': user,
				'time': time
			}
		)

	# receive message from the chat websocket.send(event=data)
	def chat_message(self, even):
		message = even['message']
		user = even['user']

		# send the data receive to the websocket who is going to populate to all user in chat
		self.send(text_data=json.dumps({
			'message':message,
			'user':user,
			'time':datetime.datetime.now().strftime("%H:%M:%S %p")# dd/mm/YY H:M:S
			# 'time':datetime.datetime.now().strftime("%b/%d/%Y %H:%M:%S")# dd/mm/YY H:M:S
			}))		

	def create_chat_message(self, message, chatGroupeName):
		me = self.scope['user']
		print(me)
		return Message_In_box.objects.create(author =me, message=message, chat_room_message_name=chatGroupeName)


	def disconnect(self, close_code):
		#remove the instance of the who is leaving the group from the chat groupe
		async_to_sync(self.channel_layer.group_discard)(
			self.chat_groupe_name,
			self.channel_name
			)



