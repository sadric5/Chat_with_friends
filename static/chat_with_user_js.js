

$('.hidden').hide();

$(document).ready(function(){
	$(".card-header").each(function(){
		
		if ($(this).text().trim()==$(".user_hide").text()) {

			$(this).parent().addClass("my-margin");
		} else{
			$(this).parent().addClass("your-margin");
		}
	});

	//don't display empty message
	$('.card-text').each(function(){
			if ($(this).text().length == 0) {
				$(this).parent().parent().hide();
		}
	})
	
});

	