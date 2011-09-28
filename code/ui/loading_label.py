#main.pyw

def _buildWebView(self):
	#...
  self.connect(self.simulator, SIGNAL("loadingPage()"), self._onLoadingPage)
  self.connect(self.simulator, SIGNAL("pageLoaded()"), self._onPageLoaded)
  self.connect(self.simulator.picker, SIGNAL("pathPicked(PyQt_PyObject)"), self._onPathPicked)
 	#...

def _onLoadingPage(self):
	self.loadingLabel.show()