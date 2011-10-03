def data(self, index, role):
	if not index.isValid():
	    return QVariant()

	item = index.internalPointer()
	if role == Qt.DisplayRole:
	    return QVariant(item.value)
	if role == Qt.UserRole:
	    if item:
	        return item.value
	if role == Qt.BackgroundRole:
	    if isinstance(item.action, AssertAction):
	        if item.action.passed == True: 
	            return QVariant(QBrush(QColor("lightgreen")))
	        elif item.action.passed == False:
	            return QVariant(QBrush(QColor("red")))
	    elif isinstance(item.action, UserAction):
	        if item.action.error == True: 
	            return QVariant(QBrush(QColor("yellow")))
	return QVariant()