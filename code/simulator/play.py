def play(self, playActions):
	self.startSimulation.emit()
	for index, action in enumerate(playActions):
	    modelIndex = self.actionsModel.index(index, 0, QModelIndex())
	    self.startPlayAction.emit(index)
	    try:
	        action.execute(self)
	        self.actionsModel.actions[index].passed = True
	    except AssertException:
	        self.actionsModel.actions[index].passed = False
	    self.actionsModel.emit(SIGNAL('dataChanged(QModelIndex, QModelIndex)'), modelIndex, modelIndex)
	    self.endPlayAction.emit(index)
	self.endSimulation.emit()      