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
       {
       	labelID = $(this).attr('for');
       }
       labelID = labelID+'-'+random;
       $('#'+labelID).trigger('click');
       $.get("/questionmaker",function(data){
		$("#card-id-"+random).html(data);
		$("#card-id"+random).append('<input type="submit" id="send" />')
		$("#card-id-"+random).css('background-color','white');
	});
   });
	$("#send").click(function(){
	if($(".answer").attr('type')=='radio'){
	var formdata = {
		q_id:$("#Question").val(),
		answer:$("input[type='radio']:checked").val()
	}
}
	else if($(".answer").attr('type') == 'text'){
	var formdata = {
		q_id:$("#Question").val(),
		answer:$("#answer").val()
	}
}
console.log(formdata);
	$.ajax({
		type:"POST",
		url:"/post",
		contentType: "application/x-www-form-urlencoded; charset=UTF-8",
		// json_string:JSON.stringify(formdata,null,'\t')
		data:formdata,
		success:function(result){
			$(".card-box").css("background-color",result.color);
		}});
	return false;	
	});
});



