'''
The analyzer module defines functions to analyze a circuit to find paths and meshes and to define the equations that describe the circuit.

'''
import sympy
def countConnections(Node):
	return len(Node.Connections)

def SeriesEquivalent(Path):
	'''Calculates the sum of resistances in a series path. Path is a list of components'''
	Rtot = 0
	for R in Path:
		Rtot += sympy.sympify(R.Impedance)

	return Rtot

def ParallelEquivalent(Components):
	'''Calculates the equivalent impedance of a set of resistors. Components is the set of components that share two nodes.'''
	N = 1
	Rtot = sympy.sympify(Components[0].Impedance)
	for R in Components[1:]:
		im = sympy.sympify(R.Impedance)
		Rtot = (Rtot*im)/(Rtot + im)
	return Rtot

def calcCurrent(Component):
	try:
		int(Component.V)
	except:
		Current = (Component.Nodes[0].V-Component.Nodes[1].V)/sympy.sympify(Component.Impedance)
		Component.setCurrent(Current)

def calcVoltage(Component):
	try:
		int(Component.I)
	except:
		Voltage = (Component.Nodes[0].V-Component.Nodes[1].V)
		Component.setVoltage(Voltage)

def KirchoffCurrentLaw(Node):
	pass

def KirchoffVoltageLaw(Path):
	pass

def OhmsLaw(Component):
	try:
		Component.Impedance
	except AttributeError:
		print ("Ohms Law does not apply to this item.")
