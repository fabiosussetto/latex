$('select').live('change',function(){
  var $this = $(this);
  var builder = new SelectorBuilder();
  var selector = builder.buildPath($this);
  var value = $this.val();
  var displayOption = $('option[value=' + value + ']', $this).text();
  labelText = _findLabel($this);
  _Logger.select(selector, value, labelText, displayOption);
});