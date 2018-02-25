import Component
class Supply(Component.Component):
	def __init__(self, Name, V = 0, I = 0, F = 0):
		self.Name = Name
		self.MaxConnections = 2
		self.Nodes = []
		self.VSupply = V
		self.ISupply = I
		self.Frequency = FF

class DCVoltageSupply(Component.Component):
	'''
	Class to define a DC voltage supply. The voltage specified is the constant output of the supply.
	'''
	def __init__(self, Name, V):
		'''
		Basic Constructor. Sets MaxConnections to 2 and Nodes to empty.
		'''
		self.Name = Name
		self.MaxConnections = 2
		self.Nodes = []
		self.VSupply = V
		self.Frequency = 0

class ACVoltageSupply(Component.Component):
	'''
	Class to define an AC voltage supply. The voltage supplied is a waveform output with peak voltage V and frequency F. Calling

	.. code-block:: python 

	  Vs = ACVoltageSupply(120, 60)
	
	Will create a 120V 60Hz Voltage supply in the circuit. 
	'''
	def __init__(self, Name, V, F):
		'''
		Basic Constructor. Sets MaxConnections to 2 and Nodes to empty.
		'''
		self.Name = Name
		self.MaxConnections = 2
		self.Nodes = []
		self.VSupply = V
		self.Frequency = F

class DCCurrentSupply(Component.Component):
	'''
	Class to define a DC Current supply. The current specified is the constant output of the supply.
	'''
	def __init__(self, Name, I):
		'''
		Basic Constructor. Sets MaxConnections to 2 and Nodes to empty.
		'''
		self.Name = Name
		self.MaxConnections = 2
		self.Nodes = []
		self.ISupply = I
		self.Frequency = 0

class ACCurrentSupply(Component.Component):
	'''
	Class to define an AC Current supply. The voltage supplied is a waveform output with peak current I and frequency F. Calling

	.. code-block:: python 

	  Vs = ACCurrentSupply(10, 60)
	
	Will create a 10A 60Hz Current supply in the circuit. 
	'''
	def __init__(self, Name, I, F):
		'''
		Basic Constructor. Sets MaxConnections to 2 and Nodes to empty.
		'''
		self.Name = Name
		self.MaxConnections = 2
		self.Nodes = []
		self.ISupply = I
		self.Frequency = F