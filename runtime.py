import threading
class Runtime:
	threads = {}
	modules = {}
	@staticmethod
	def attach(module):
		Runtime.modules[module.id] = module
		Runtime.threads[module.id] = threading.Thread(None,module.thread)
		Runtime.threads[module.id].daemon = True
		Runtime.threads[module.id].start()
	@staticmethod
	def detach(id):
		Runtime.modules[id].terminate = True
		del Runtime.modules[id]
		del Runtime.threads[id]