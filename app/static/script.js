if (screen.width <= 800) {
		window.location = "";
	  }
var labelID;
var random;



$(document).ready(function(){
	$('label').click(function() {		
       	labelID = $(this).attr('for');
       
        $('#'+labelID).trigger('click', function(){

            if(booRadio == this){
                this.checked = false;
        booRadio = null;
            }else{
            booRadio = this;
        }
    });
       
       $.get("/questionmaker",function(data){
		$("#card-id-1").html(data);
		$("#card-id-1").css('background-color','white');
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
	$.ajax({
		type:"POST",
		url:"/post",
		contentType: "application/x-www-form-urlencoded; charset=UTF-8",
		// json_string:JSON.stringify(formdata,null,'\t')
		data:formdata,
		success:function(result){
			$("#place").css("background-color",result.color);
			if(result.color == "green"){
		$.get("/questionmaker",function(data){
		$("#card-id-1").html(data);
		$("#card-id-1").css('background-color','white');
	});
			}
		}});
	return false;	
	});
});



