def setupModelData(self):  
  for action in self.actions:
  	self.addItem(action) 

def addItem(self, action):    
	newparent = TreeItem(TreeItem.MAIN_NODE, action.description, self.rootItem, action)

	if not isinstance(action, VisitAction):
	    newparent.appendChild(TreeItem(TreeItem.DETAIL_NODE, "Selector: %s" % action.selector, newparent))

	if isinstance(action, AssertContentAction):
	    newparent.appendChild(TreeItem(TreeItem.DETAIL_NODE, "Value: %s" % action.value, newparent))
	elif isinstance(action, AssertPresenceAction):
	    newparent.appendChild(TreeItem(TreeItem.DETAIL_NODE, "Check visibility: %s" % action.checkVisibility, newparent))
	elif isinstance(action, FillAction):
	    newparent.appendChild(TreeItem(TreeItem.DETAIL_NODE, "Value: %s" % action.value, newparent)) 
	elif isinstance(action, VisitAction):
	    newparent.appendChild(TreeItem(TreeItem.DETAIL_NODE, "Url: %s" % action.url, newparent))       
	self.parents.append(newparent)
	self.rootItem.appendChild(newparent)