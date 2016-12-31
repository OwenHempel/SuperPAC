class Circuit:
	'''
	Class to define a Circuit object, which will be initialized empty and filled in as the circuit elements are placed.

	'''
	def __init__(self):
		self.Components = {}
		self.Nodes = {}

	def addNode(self, Node):
		if Node.Name in self.Nodes:
			print("Error, That node name is already taken in this circuit!")
		else: 
			self.Nodes[Node.Name] = Node

	def addComponent(self, Component):
		if Component.Name in self.Nodes:
			print("Error, That component name is already taken in this circuit!")
		else: 
			self.Components[Name] = Node

	def SeriesEquivalent(self, Components):
		'''Calculates the sum of resistances in a series path. Path is a list of components'''
		Rtot = 0
		for Component in Components:
			Rtot += sympy.sympify(R.Impedance)
		return Rtot

	def ParallelEquivalent(self, Components):
		'''Calculates the equivalent impedance of a set of resistors. Components is the set of components that share two nodes.'''
		Rtot = sympy.sympify(Components[0].Impedance)
		for R in Components[1:]:
			im = sympy.sympify(R.Impedance)
			Rtot = (Rtot*im)/(Rtot + im)
		return Rtot

	def calcCurrent(self, Component):
		try:
			int(Component.V)
		except:
			Current = (Component.Nodes[0].V-Component.Nodes[1].V)/sympy.sympify(Component.Impedance)
			Component.setCurrent(Current)

	def calcVoltage(self, Component):
		try:
			int(Component.I)
		except:
			Voltage = (Component.Nodes[0].V-Component.Nodes[1].V)
			Component.setVoltage(Voltage)

	def reduce(self, Node):
		for Component in Node.Connections:
			for Component2 in Node.Connections.remove(Component)
				if Component.isSeries(Component2):
					pass
				if Component.isParallel(Component2):
					pass

