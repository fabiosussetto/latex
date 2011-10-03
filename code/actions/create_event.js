mouseEvent: function(type, options) {  
	var evt;
	var e = $.extend({
		bubbles: true, cancelable: (type != "mousemove"), view: window, detail: 0,
		screenX: 0, screenY: 0, clientX: 0, clientY: 0,
		ctrlKey: false, altKey: false, shiftKey: false, metaKey: false,
		button: 0, relatedTarget: undefined
	}, options);

	var relatedTarget = $(e.relatedTarget)[0];

	evt = document.createEvent("MouseEvents");
	evt.initMouseEvent(type, e.bubbles, e.cancelable, e.view, e.detail,
		e.screenX, e.screenY, e.clientX, e.clientY,
		e.ctrlKey, e.altKey, e.shiftKey, e.metaKey,
		e.button, e.relatedTarget || document.body.parentNode
	);      
	
	return evt;
}  