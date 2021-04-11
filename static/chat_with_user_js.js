

console.log($(".hidden").text());

$('.hidden').hide();
$('.hidden').addClass('hiThere');


$(document).ready(function(){
	$(".card-header").each(function(i){
		// var name= $(this).text().trim();
		// console.log(i+':'+ name.length);

		if ($(this).text().trim()==$(".hidden").text()) {

			$(this).parent().addClass("my-margin");
		} else{
			$(this).parent().addClass("your-margin");
		}
	});
	
});

	// document.querySelector('#id_my_messages').focus();
