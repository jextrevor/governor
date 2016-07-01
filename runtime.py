import threading
class Runtime:
	threads = {}
	modules = {}
	@staticmethod
	def attachall():
		from governor.module import Module
		for s in Module.modulelist:
			if s.id not in Runtime.modules:
				attach(s)
	@staticmethod
	def attach(module):
		Runtime.modules[module.id] = module
		Runtime.threads[module.id] = threading.Thread(None,module.thread)
		Runtime.threads[module.id].daemon = True
		Runtime.threads[module.id].start()
	@staticmethod
	def static(module):
		Runtime.modules[module.id] = module
		Runtime.threads[module.id] = threading.Thread(None,module.thread)
		Runtime.threads[module.id].start()
	@staticmethod
	def detach(id):
		Runtime.modules[id].terminate = True
		del Runtime.modules[id]
		del Runtime.threads[id]