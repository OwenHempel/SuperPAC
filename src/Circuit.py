import sympy
import AnalogComponent

class Circuit:
	'''
	Class to define a Circuit object, which will be initialized empty and filled in as the circuit elements are placed.

	'''
	def __init__(self):
		self.Components = {}
		self.Nodes = {}

	def addNode(self, Node):
		'''Adds the component to the circuit. GOTCHA: Ensuring the ID is unique is not handled here!'''
		NodeID = len(self.Nodes)
		self.Nodes[NodeID] = Node

	def addComponent(self, Component):
		'''Adds the component to the circuit. GOTCHA: Ensuring the ID is unique is not handled here!'''
		ComponentID = len(self.Components)
		self.Components[ComponentID] = Component

	def removeNode(self, Node):
		if Node in [self.Nodes[NodeID] for NodeID in self.Nodes]:
			del self.Nodes[NodeID]


	def SeriesEquivalent(self, Components):
		'''Calculates the sum of resistances in a series path. Path is a list of components'''
		Ztot = 0
		Name = ""
		for Component in Components:
			Ztot += Component.Impedance
			Name += Component.Name
		return AnalogComponent.AnalogComponent(Name, Z = Ztot)

	def ParallelEquivalent(self, Components):
		'''Calculates the equivalent impedance of a set of resistors. Components is the set of components that share two nodes.'''
		Zinv = 0
		Ztot = 0
		Name = ""
		for Component in Components:
			Name += Component.Name
			Zinv += Component.Impedance**-1
			Ztot = Zinv**-1
		return AnalogComponent.AnalogComponent(Name, Z = Ztot)

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
		Targets = Node.Connections
		for Component in Targets:
			Targets.remove(Component)
			for Component2 in Targets:
				if Component.isParallel(Component2):
					Equivalent = self.ParallelEquivalent([Component, Component2])
				elif Component.isSeries(Component2):
					Equivalent = self.SeriesEquivalent([Component, Component2])
				else:
					pass
				print(Equivalent.Name, Equivalent.Impedance, Equivalent.Nodes)


