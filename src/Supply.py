import Component

class DCVoltageSupply(Component.Component):
	'''
	Class to define a DC voltage supply. The voltage specified is the constant output of the supply.
	'''
	def __init__(self, V):
		'''
		Basic Constructor. Sets MaxConnections to 2 and Nodes to empty.
		'''
		self.MaxConnections = 2
		self.Nodes = []
		self.VSupply = V

class ACVoltageSupply(Component.Component):
	'''
	Class to define an AC voltage supply. The voltage supplied is a waveform output with peak voltage V and frequency F. Calling

	.. code-block:: python 

	  Vs = ACVoltageSupply(120, 60)
	
	Will create a 120V 60Hz Voltage supply in the circuit. 
	'''
	def __init__(self, V, F):
		'''
		Basic Constructor. Sets MaxConnections to 2 and Nodes to empty.
		'''
		self.MaxConnections = 2
		self.Nodes = []
		self.VSupply = V
		self.Frequency = F

class DCCurrentSupply(Component.Component):
	'''
	Class to define a DC Current supply. The current specified is the constant output of the supply.
	'''
	def __init__(self, I):
		'''
		Basic Constructor. Sets MaxConnections to 2 and Nodes to empty.
		'''
		self.MaxConnections = 2
		self.Nodes = []
		self.ISupply = I

class ACCurrentSupply(Component.Component):
	'''
	Class to define an AC Current supply. The voltage supplied is a waveform output with peak current I and frequency F. Calling

	.. code-block:: python 

	  Vs = ACCurrentSupply(10, 60)
	
	Will create a 10A 60Hz Voltage supply in the circuit. 
	'''
	def __init__(self, I, F):
		'''
		Basic Constructor. Sets MaxConnections to 2 and Nodes to empty.
		'''
		self.MaxConnections = 2
		self.Nodes = []
		self.ISupply = I
		self.Frequency = F