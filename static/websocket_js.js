var username = JSON.parse(document.getElementById('room-name').textContent);
	const chat_socket = new WebSocket(
		'ws://'
		+ window.location.host
		+ '/ws/chat/'
		+ document.querySelector('.chatuser').textContent.trim()
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
						if($('.user_hide').text().trim()==user){
							return 'my-margin';
						}else{
							return 'your-margin';
						}
					}

					p_element.innerHTML +=

					`
					<div class= "card mt-2 mb-2 message-card ${you()} container-fluid">

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
		message_send.value = '';
	};