import Component

class DigitalComponent(Component.Component):
	'''
	Class to describe all digital components. Only three types exist: Resistors, Capacitors, and Inductors. This module is designed to be extensible to include other types. Unless overridden by a subclass, Analog components will be limited to two connections.
	'''
	def __init__(self):
		'''
		Basic Constructor. Sets MaxConnections to 2 and Nodes to empty.
		'''
		self.MaxConnections = 2
		self.Nodes = []

class Switch(DigitalComponent):
	'''
	Class for a switch. Transfer function is a purely proportional relation. Initializes to Single Pole, Single throw. These can be 
	'''
	def __init__(self, Poles = 1, Throws = 1, State = False):
		self.MaxConnections = (Poles+1)*Throws
		self.Nodes = []
		self.state = State