if (screen.width <= 800) {
		window.location = "";
	  }
var labelID;
var random;

$(document).ready(function(){
	$('label').click(function() {
		do
		random = Math.floor(Math.random() * 4) + 1 
		while (random <= 0)
       labelID = $(this).attr('for');
       labelID = labelID+'-'+random;
       $('#'+labelID).trigger('click');
   });
});



