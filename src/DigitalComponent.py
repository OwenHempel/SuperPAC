import Component

class DigitalComponent(Component.Component):
	'''
	Class to describe all digital components. This module is designed to be extensible to include other types.
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
		self.State = State

class Relay(DigitalComponent):
	'''
	Class for a relay. Has 2 special connections for the Coil. Has a number of contact sets, each initialized to a Normal state. If the voltage across the coil contacts exceeds the coil voltage parameter, the states of all contacts are inverted
	'''
	def __init__(self, CoilVoltage = None, State = False)

		self.NormalOpenContacts