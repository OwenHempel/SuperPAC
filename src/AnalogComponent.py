import Component
import numpy

class AnalogComponent(Component.Component):
	'''
	Class to describe all analog components. Only three types exist: Resistors, Capacitors, and Inductors. This module is designed to be extensible to include other types. Unless overridden by a subclass, Analog components will be limited to two connections.
	The direction of current flow is left undefined and decided by the analyzer.
	'''
	def __init__(self, Name, R = 0, L = 0, C = 0, Z = 0):
		'''
		Basic Constructor. Sets MaxConnections to 2 and Nodes to empty.
		'''
		self.MaxConnections = 2
		self.Name = Name
		self.Nodes = []
		self.I = None
		self.V = None
		self.R = R
		self.C = C
		self.L = L
		if Z == 0:
			self.calcImpedance()
		else:
			self.Impedance = Z


	def setCurrent(self, I):
		self.I = I
	def calcImpedance(self):
		self.Impedance = self.R + self.L*1j
		if not(self.C == 0):
			self.Impedance += -1j*self.C**-1
	def setVoltage(self, V):
		self.V = V

class Resistor(AnalogComponent):
	'''
	Class for a resistor. Impedance is a purely proportional relation. Resistance in Ohms.
	'''

	def __init__(self, R, Name):
		self.Name = Name
		self.MaxConnections = 2
		self.Nodes = []
		self.R = float(R)
		self.L, self.C = 0, 0
		self.I = None
		self.V = None
		self.calcImpedance()

class Capacitor(AnalogComponent):
	'''
	Class for a capacitor. Capacitance in microFarads.
	'''
	def __init__(self, C, Name):
		self.Name = Name
		self.MaxConnections = 2
		self.Nodes = []
		self.C = float(C)
		self.R, self.L = 0,0
		self.calcImpedance()
		self.I = None
		self.V = None

class Inductor(AnalogComponent):
	'''
	Class for an Inductor. Inductance in milliHenrys.
	'''
	def __init__(self, L, Name):
		self.Name = Name
		self.MaxConnections = 2
		self.Nodes = []
		self.L = float(L)
		self.R, self.C = 0,0
		self.calcImpedance()
		self.I = None
		self.V = None

		
