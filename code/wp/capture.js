$('a').each(function(){ 
  this.addEventListener('click', function(){
    var $this = $(this);
    var builder = new SelectorBuilder();
    var selector = builder.buildPath($this);
    _Logger.link(selector, $this.text().replace(/[\s]{2,}/g, ' '));  
  }, true);
});