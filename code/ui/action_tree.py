def _buildActionsTree(self):
  self.treeWidget = QTreeView()
  self.treeWidget.setModel(self.actionsModel)
  self.connect(self.simulator, SIGNAL("startPlayAction(int)"), self._onStartPlayAction)
  self.btnRemoveAction = QToolButton()
  self.btnRemoveAction.setText('-')
  self.connect(self.btnRemoveAction, SIGNAL("clicked()"), self._onRemoveActionClicked)
  self.btnPlayAction = QToolButton()
  self.btnPlayAction.setText('Play')
  self.connect(self.btnPlayAction, SIGNAL("clicked()"), self._onPlayActionClicked)              

def _onPlayActionClicked(self):
  self.simulator.play(self.actionsModel.actions)      

def _onRemoveActionClicked(self):                                         
  self.actionsModel.removeRows(self.treeWidget.currentIndex().row())