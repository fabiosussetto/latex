self.networkManager = self.webpage.networkAccessManager()
self.connect(self.networkManager, SIGNAL('finished(QNetworkReply *)'), self._on_network_finished)
#...

def _on_network_finished(self, reply):
	request = reply.request()
  ajax_header = request.rawHeader(QByteArray("X-Requested-With"))
  if not ajax_header.isEmpty() and QString(ajax_header).compare("XMLHttpRequest", Qt.CaseInsensitive) == 0:
      self._load_status = True