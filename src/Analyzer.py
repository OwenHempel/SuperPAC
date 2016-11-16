'''
The analyzer module defines functions to analyze a circuit to find paths and meshes and to define the equations that describe the circuit.

'''
import sympy.Symbol


def KirchoffCurrentLaw(Node):


def KirchoffVoltageLaw(Path):

def OhmsLaw(Component):
	try:
		Component.Impedance
	except AttributeError:
		print ("Ohms Law does nto apply to this item.")
