



class Node:
	'''
	**Description:** Class defining a circuit node, which is the intersection of two or components. A node has N Connections, where N is the number of connected components. If a component does not have a node to attach to, a new node will be created.
	Has the following properties:

	* Connections: Defines which Connections are connected to the node.
	* Voltage: If set, The node's reference voltage is held at this value. 
	'''
	def __init__(self):
		from sympy import Symbol
		'''
		Constructor method for the class. Initializes to no Connections, and voltage set to None.
		'''
		self.Connections  = []
		self.V = Symbol('v')
		print("Node Created")

	def Nconnect(self, component):
		'''
		Args:

		Returns: 
			Status (String): Describes the status of the connection (successful or otherwise)

		Method to add a component to the node, if it is not already connected to the node. 
		'''
		if component not in self.Connections:
			self.Connections.append(component)
			return "Success. Component Connected."

		else:
			return "Error. Component already connected to specified node."		

	def Ndisconnect(self, component):
		'''
		Returns: 
			Status (String): Describes the status of the connection (successful or otherwise)

		Method to disconnect a component from the node, if it is connected.		
		'''
		if component in self.Connections:
			self.Connections.remove(component)
			return "Success. Component Disconnected."

		else:
			return "Error. Component not connected to specified node."

	def getConnections(self):
		'''
		Returns:
			Connections (List): List of all Connections connected to the node

		Accessor. Returns all of the Connections connected to the node in a list
		'''
		return self.Connections

	def setVoltage(self, Voltage):
		'''
		Mutator. Sets the voltage to the supplied value.
		'''
		self.V = Voltage

	def ground(self):
		'''
		Mutator. Sets the voltage to ground (0).
		'''
		self.setVoltage(0)
