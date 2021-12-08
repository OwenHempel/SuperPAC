class Path:
	'''**Description:** Class defining a circuit path, which is a set of components that form a complete loop. This is defined by reaching the starting point, which must be a defined node.
	Naive solution: random-walk algortihm until starting node is reached. unlikely to be efficient.
	Efficient solution: for component attached to node, generate multiple Paths and add each possibility?
	'''
	def __init__(self):
		'''
		Basic constructor. Initializes with Components empty.
		'''
		self.StartNode = None
		self.Components = []
	
	def setStartNode(self, Node):
		'''Args: Node (Node)
		Returns: None
		Set the starting node for the path.'''
		self.StartNode = Node

	def addComponent(self, Component):
		'''Args: Component (Component)
		Returns: None
		Adds Component to path.'''
		self.Components.append(Component)