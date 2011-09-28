def wait_load(self, timeout=10):     
  app = QApplication.instance()
  app.processEvents()
  if self._load_status is not None:
      load_status = self._load_status
      self._load_status = None
      return load_status
  start_time = time.time()
 
  while self._load_status is None:
      if timeout and time.time() - start_time > timeout:
          raise SimulatorTimeout("Timeout reached: %d seconds" % timeout)
      app.processEvents()
 
  app.processEvents()    
  load_status = self._load_status
  self._load_status = None
  return load_status                

def _on_load_finished(self, successful):
  self._load_status = successful
  self.pageLoaded.emit()
  self.load_js()