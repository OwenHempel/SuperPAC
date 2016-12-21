class Component:
	'''
	Circuit Component Base class. provides the absolute minimum to meet the definition of a component in a circuit.
	'''
	def __init__(self):
		'''
		Basic Constructor. Sets MaxConnections to 0 and Nodes to empty.
		'''
		self.MaxConnections = 0
		self.Nodes = []

	def connect(self, Node):
		'''
		Adds a Node to the component's nodes, if there is a connection available.
		'''
		if len(self.Nodes) < self.MaxConnections:
			status = Node.Nconnect(self)
			if status.startswith("Success"):
				self.Nodes.append(Node)
				

		else:
			status = "All Component connections taken"

		print(status)

	def disconnect(self, Node):
		'''
		Removes a Node from the component's nodes.
		'''
		status = Node.Ndisconnect(self)
		if status.startswith("Success"):
			self.Nodes.remove(Node)

		print(status)

	def setMaxConnections(self, N):
		'''
		Changes the Max Connections to the supplied value.
		'''
		self.MaxConnections = N

	

