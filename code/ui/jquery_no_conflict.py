def load_jquery(self, force=False):    
	 """Load jquery in the current frame"""
	jscode = self.jquery
	jscode += "\nvar %s = jQuery.noConflict();" % self.jQueryAlias
	self.runjs(jscode)