
$(function(){
	var current_page = window.location.href.split("/")[3]
	switch(current_page.toLowerCase()) {

		case "services":
		$("#services").addClass("active")
		break;

		case "area":
		$("#area").toggleClass("active")
		break;

		case "about":
		$("#about").addClass("active")
		break;

		case "contact":
		$("#contact").toggleClass("active")
		break;

		case "gallery":
		$("#gallery").toggleClass("active");
		break;

		case "careers":
		$("#careers").toggleClass("active");
		break;

		default:
		$("#home").toggleClass("active");
		break;
	}; 


	
	


	});





});

