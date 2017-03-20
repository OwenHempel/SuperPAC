#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
if __name__ == "__main__":
	import AnalogComponent
	import Node
	import Supply
	import Circuit
	import sympy


	R1 = AnalogComponent.Resistor(8, 'R1')
	R2 = AnalogComponent.Resistor(8, 'R2')
	C2 = AnalogComponent.Capacitor(1000, 'C2')
	C1 = AnalogComponent.Capacitor(1000, 'C1')
	L1 = AnalogComponent.Inductor(5, 'L1')
	L2 = AnalogComponent.Inductor(5, 'L2')
	V1 = Supply.DCVoltageSupply(12)


	Cct = Circuit.Circuit()

	N1 = Node.Node(sympy.Symbol('V1'))
	Cct.addNode(N1)
	N2 = Node.Node(sympy.Symbol('V2'))
	Cct.addNode(N2)
	N3 = Node.Node(sympy.Symbol('V3'))
	Cct.addNode(N3)
	N4 = Node.Node(sympy.Symbol('V4'))
	Cct.addNode(N4)

	R1.connect(N1)
	R1.connect(N2)
	C1.connect(N1)
	C1.connect(N3)
	C2.connect(N3)
	C2.connect(N4)

	R2.connect(N2)
	R2.connect(N3)

	N3.ground()

	Cct.addComponent(R1)
	Cct.addComponent(R2)
	Cct.addComponent(C1)
	Cct.addComponent(C2)

	print ( [Cct.Components[Key].Name for Key in Cct.Components])
	for node in [Cct.Nodes[ID] for ID in Cct.Nodes]:
		Cct.reduce(node)


