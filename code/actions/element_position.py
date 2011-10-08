def getElementPosition(self, selector):
   jscode = "_off = %s('%s').offset();_off.left+','+_off.top" % (self.jQueryAlias, selector)
   x, y = ("%s" % self.runjs(jscode).toString()).split(',')
   point = QPoint(int(x), int(y))
   rect = self.webframe.geometry()
   where = QPoint(rect.x() + point.x() + 5, rect.y() + point.y() + 2)
   return where                     