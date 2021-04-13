

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


	//don't display empty message
	$('.card-text').each(function(){
		// alert($(this).text().length);
			if ($(this).text().length == 0) {
				$(this).parent().parent().hide();
		}
	})
	
});

	
