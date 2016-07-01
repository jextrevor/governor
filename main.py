from governor.runtime import Runtime
from governor.module import Module
class AndGate(Module):
	def __init__(self):
		Module.__init__(self)
		self.specs=["Signal"]
		self.signal = 0
	def run(self):
		inputs = findspecs("Signal")
		if len(inputs) == 2:
			if self.lock(inputs[0].id) == True and self.lock(inputs[1].id) == True:
				if inputs[0].signal == 1 and inputs[1].signal == 1:
					self.signal = 1
					self.release()
					return
		self.signal = 0
		self.release()
class OrGate(Module):
	def __init__(self):
		Module.__init__(self)
		self.specs=["Signal"]
		self.signal = 0
	def run(self):
		inputs = findspecs("Signal")
		if len(inputs) == 2:
			if self.lock(inputs[0].id) == True and self.lock(inputs[1].id) == True:
				if inputs[0].signal == 1 or inputs[1].signal == 1:
					self.signal = 1
					self.release()
					return
		self.signal = 0
		self.release()
class XorGate(Module):
	def __init__(self):
		Module.__init__(self)
		self.specs=["Signal"]
		self.signal = 0
	def run(self):
		inputs = findspecs("Signal")
		if len(inputs) == 2:
			if self.lock(inputs[0].id) == True and self.lock(inputs[1].id) == True:
				if inputs[0].signal == 1 or inputs[1].signal == 1:
					if inputs[0].signal == 0 or inputs[1].signal == 0:
						self.signal = 1
						self.release()
						return
		self.signal = 0
		self.release()
class Inverter(Module):
	def __init__(self):
		Module.__init__(self)
		self.specs=["Signal"]
		self.signal = 0
	def run(self):
		inputs = findspecs("Signal")
		if len(inputs) == 1:
			if self.lock(inputs[0].id) == True:
				if inputs[0].signal == 0:
					self.signal = 1
					self.release()
					return
		self.signal = 0
		self.release()
class Switch(Module):
	def __init__(self):
		Module.__init__(self)
		self.specs=["Signal,Input"]
		self.name = ""
		self.signal = 0
	def switch(self):
		if self.signal == 0:
			self.signal = 1
		else:
			self.signal = 0
class Lightbulb(Module):
	def __init__(self):
		Module.__init__(self)
		self.signal = 0
		self.specs=["Output"]
		self.name = ""
	def run(self):
		inputs = findspecs("Signal")
		if len(inputs) == 1:
			if self.lock(inputs[0].id) == True:
				if inputs[0].signal == 1:
					self.signal = 1
					self.release()
					return
		self.signal = 0
		self.release()
class Console(Module):
	def run(self):
		inputs = self.findspecs("Input")
		outputs = self.findspecs("Output")
		for i in inputs:
			if self.lock(i.id) == False:
				return
		for i in outputs:
			if self.lock(i.id) == False:
				return
		inputstring = input("->")
		if inputstring == "list":
			print("Inputs:")
			for i in inputs:
				print(i.name)
			print("Outputs:")
			for i in outputs:
				print(i.name)
			return
		if inputstring == "set":
			newvalue = 0
			value = input("*>")
			if value == "1":
				newvalue = 1
			key = input("?>")
			for i in inputs:
				if key == i.name:
					i.signal = newvalue
					return
		if inputstring == "get":
			key = input("?>")
			for i in inputs:
				if key == i.name:
					print(i.signal)
					return
			for i in outputs:
				if key == i.name:
					print(i.signal)
					return
		if inputstring == "quit":
			self.terminate = True
input1 = Switch()
input2 = Switch()
gate = XorGate()
output1 = Lightbulb()
console = Console()
input1.name = "input1"
input2.name = "input2"
output1.name = "output1"
gate.attach(input1)
gate.attach(input2)
output1.attach(gate)
console.attach(input1)
console.attach(input2)
console.attach(output1)
Runtime.attach(gate)
Runtime.attach(output1)
Runtime.static(console)