'''
The analyzer module defines functions to analyze a circuit to find paths and meshes and to define the equations that describe the circuit.

'''
import sympy




def KirchoffCurrentLaw(Node):
	pass

def KirchoffVoltageLaw(Path):
	pass

def OhmsLaw(Component):
	try:
		Component.Impedance
	except AttributeError:
		print ("Ohms Law does not apply to this item.")
