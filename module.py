import time
class Module:
	id = 0
	def __init__(self):
		self.id = Module.id
		self.modules = {}
		self.usenotify = {}
		self.delnotify = {}
		self.specs = []
		self.terminate = False
		Module.id += 1
	def run(self):
		pass
	def thread(self):
		while self.terminate == False:
			self.run()
		self.terminate = False
	def attach(self,module):
		self.modules[module.id] = module
		self.usenotify[module.id] = 0
		self.delnotify[module.id] = False
	def lock(self,id):
		if id in self.modules:
			if self.delnotify[id] == False:
				self.usenotify[id] += 1
				return True
			else:
				return False
		else:
			return False
	def query(self, spec):
		returnlist = self.findspecs(spec)
		if returnlist != False:
			if len(returnlist) == 1:
				return2 = self.lock(returnlist[0].id)
				if return2 == True:
					return returnlist[0]
				else:
					return False
			else:
				return False
		else:
			return False
	def unlock(self,id):
		self.usenotify[id] -= 1
		if self.usenotify[id] < 0:
			self.usenotify[id] == 0
	def detach(self,id):
		self.delnotify[id] = True
		while self.usenotify[id] != 0:
			pass
		del self.modules[id]
		del self.usenotify[id]
		del self.delnotify[id]
	def findspecs(self, spec):
		returnlist = []
		for s in self.modules.values():
			if spec in s.specs:
				returnlist.append(s)
		if len(returnlist) > 0:
			return returnlist
		else:
			return False