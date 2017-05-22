
function showtips(obj, str) {  //obj对象中必须包含id，str(需要提示的内容)

	if (obj.id == "") {

		$(obj).mouseout(function () {

			$("#followtip").remove();

		});

		$(obj).mousemove(function (e) {

			//$("#followtip").remove();

			if ($("#followtip").html() == null) {

				if (str == "") { str = $("#" + obj.id).html(); } //

				var toolTip = "<div id='followtip'  style='position:absolute;width:700px; border:solid #aaa 1px;background-color:#00F5FF;font-size:13px;color:black;padding-left: 5px'>" + str + "</div>";

				$("body").append(toolTip); //

				$("#followtip").css({

					"top": e.pageY + "px",

					"left": e.pageX + "px"

				});

				$(obj).mouseout(function () {

					$("#followtip").remove();

				});

				$(obj).mousemove(function (e) {  

					var numWidth = document.body.clientWidth;

					var numHeight = document.body.clientHeight;

					var clinety = event.clientY;

					var clinetx = event.clientX;

					$("#followtip").css({

						"left": (e.pageX - 0) +12+ "px"});


					if (numHeight - $("#followtip").height - clinety > 0) {

						$("#followtip").css({ "top": (e.pageY - 0) + "px" });

					}

					else {

						$("#followtip").css({ "top": (e.pageY - $("#followtip").height()) + "px" });

					}
				});
			}
		})
	}
} 



$(document).on("mouseover",".itemid",function(){
	var item_id=$(this).html();
	var myobj=this;
	$.ajax({
		type: "post",
		dataType: "text",
		url: "/rewardserver/get_item_msg|"+item_id+"/",
		data: {},
		success: function(msg){
			showtips(myobj,msg);

		}
	});




}); 

$(document).on("click",".itemid",function(){

	var item_id=$(this).html();
	$.ajax({
		type: "post",
		dataType: "text",
		url: "/search/",// 
		data: {'searchxls':'allitemdict', 'searchtext':item_id,'searchtype':1,'opt1':0,'opt2':0},

		success: function(msg){

			$("#detail").html(msg);
			var c = window.document.body.scrollHeight;
			window.scroll(0,c); 

		}
	});
}); 

$(document).on("click",".rewardid",function(){

	var rewardid=$(this).html();
	$.ajax({
		type: "post",//
		dataType: "text",//
		url: "/search/",// 
		data: {'searchxls':'allrewarddict', 'searchtext':rewardid,'searchtype':1,'opt1':0,'opt2':0},

		success: function(msg){

			$("#detail").html(msg);
			var c = window.document.body.scrollHeight;
			window.scroll(0,c); 

		}
	});
}); 
