
var username = JSON.parse(document.getElementById('room-name').textContent);
		
var protocl=window.location.protocol
var protocol_use = protocl=="https:"?"wss":"ws";

const chat_socket = new WebSocket(
		protocol_use
		+ "://"
		+ window.location.host
		+ ":8989"
		+ '/wss/chat/'
		+ username
		+ '/'
	)


	message_section = $(".message-container");
	p_element = document.createElement('div');
	p_element.class = 'message-container';
		



		chat_socket.onmessage = function(e){
			document.querySelector('.message-container').appendChild(p_element);
			
				message_to_socket = JSON.parse(e.data);
				if (message_to_socket['message']!='')
				{	//avoid sending empty string to the chat room.
					message_receive = message_to_socket['message'];
					user = message_to_socket['user'];
					time = message_to_socket['time'];

					function you(){
						if($('.hidden').text().trim()==user){
							return 'my-margin';
						}else{
							return 'your-margin';
						}
					}

					p_element.innerHTML +=

					`
					<h3>New Message</h3>
					<div class= "card m-2 message-card ${you()}">

					 	<div class='card-header'>
					 		${user} 
					 	</div>

						<div class='card-body'>
							<p class='card-text'> ${message_receive}</p>
						</div>

						<div class='card-footer text-muted>
							<p class='card-text'>
							 	<small class='text-muted'>
							 		${time}
							 	</small>
							</p>
						</div>

					</div>`
					;
				}	
					};
	
	chat_socket.onclose = function(e){
		console.error('chat socket closed unexpected');
	};
	// take the message
	document.querySelector('#submitiom').onclick  = function(e){
		const message_send = document.querySelector('#id_my_messages');
		const $message_send = message_send.value;
		user = document.querySelector('#usern').textContent;

		chat_socket.send(JSON.stringify({
			'message': $message_send,
			'user':user,
			'time': 'lol',
		}));
		// alert(message_send);
		message_send.value = '';
	};