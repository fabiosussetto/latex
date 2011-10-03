class ClickLinkAction(UserAction):
                                               
  def __init__(self, selector=None, label=None, xmlNode=None):
      super(ClickLinkAction, self).__init__(selector, None, label, xmlNode)
      self.description = "Click link '%s'" % self.label
      
  def execute(self, simulator):
      if not simulator.assertExists(self.selector):
          raise DomElementNotFound(self.selector)
      
      jscode = "%s('%s').simulate('click');" % (simulator.jQueryAlias, self.selector)
      simulator.runjs(jscode)
      return simulator.wait_load()
  
  def fromXML(self, node):
      super(ClickLinkAction, self).fromXML(node)
       
  def toXML(self):
      element = super(ClickLinkAction, self).toXML()
      element.set("label", self.label)
      Et.SubElement(element, "selector", {"path": self.selector})
      return element