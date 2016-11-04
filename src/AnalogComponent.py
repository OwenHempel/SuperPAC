import Component

class AnalogComponent(Component.Component):
	'''
	Class to describe all analog components. Only three types exist: Resistors, Capacitors, and Inductors. This module is designed to be extensible to include other types. Unless overridden by a subclass, Analog components will be limited to two connections.
	'''
	def __init__(self):
		'''
		Basic Constructor. Sets MaxConnections to 2 and Nodes to empty.
		'''
		self.MaxConnections = 2
		self.Nodes = []



class Resistor(AnalogComponent):
	'''
	Class for a resistor. Transfer function is a purely proportional relation. 
	'''
	def __init__(self, R):
		self.MaxConnections = 2
		self.Nodes = []
		self.R = R
