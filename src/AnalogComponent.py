import Component


class AnalogComponent(Component.Component):
	'''
	Class to describe all analog components. Only three types exist: Resistors, Capacitors, and Inductors. This module is designed to be extensible to include other types. Unless overridden by a subclass, Analog components will be limited to two connections.
	The direction of current flow is left undefined and decided by the analyzer.
	'''
	def __init__(self):
		'''
		Basic Constructor. Sets MaxConnections to 2 and Nodes to empty.
		'''
		self.MaxConnections = 2
		self.Nodes = []
		self.I = None
		self.V = None

	def setCurrent(self, I):
		self.I = I

	def setVoltage(self, V):
		self.V = V


class Resistor(AnalogComponent):
	'''
	Class for a resistor. Impedance is a purely proportional relation. Resistance in Ohms.
	'''

	def __init__(self, R):
		self.MaxConnections = 2
		self.Nodes = []
		self.R = R
		self.Impedance = str(R)
		self.I = None
		self.V = None

class Capacitor(AnalogComponent):
	'''
	Class for a capacitor. Impedance expressed in Laplace domain. Capacitance in microFarads.
	'''
	def __init__(self, C):
		self.MaxConnections = 2
		self.Nodes = []
		self.C = C
		self.Impedance = '1/(s*'+str(C)+')'
		self.I = None
		self.V = None

class Inductor(AnalogComponent):
	'''
	Class for an Inductor. Impedance expressed in Laplace domain. Inductance in milliHenrys.
	'''
	def __init__(self, L):
		self.MaxConnections = 2
		self.Nodes = []
		self.L = L
		self.Impedance = str(L)+'*s'
		self.I = None
		self.V = None

		
