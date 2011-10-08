class ClickLinkAction(UserAction):
                          
  def __init__(self, selector=None, label=None, xmlNode=None):
      super(ClickLinkAction, self).__init__(selector, None, label, xmlNode)
      self.description = "Click link '%s'" % self.label
      
  def execute(self, simulator):
      self._execute_native(simulator)
      return simulator.wait_load()
  
  def _execute_native(self, simulator):
      where = simulator.getElementPosition(self.selector)
      QTest.mouseMove(simulator.webview, where)
      QTest.mouseClick(simulator.webview, Qt.LeftButton, Qt.NoModifier, where)