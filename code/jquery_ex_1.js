$("div.test").children('a:not(:first-child)').attr('href', '#').click(function(){
	alert($(this).text());
	return false;
});