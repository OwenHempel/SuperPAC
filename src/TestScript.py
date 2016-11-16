#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5

import AnalogComponent
import Node
import Supply
import sympy

R1 = AnalogComponent.Resistor(8)
R2 = AnalogComponent.Resistor(16)

V1 = Supply.DCVoltageSupply(12)

N1 = Node.Node()
N2 = Node.Node()
N3 = Node.Node()

N3.ground()

R1.connect(N1)
R1.connect(N2)

R2.connect(N2)
R2.connect(N3)

V1.connect(N1)
V1.connect(N3)

#Analysis portion

print(type(R1))
print(type(R1)==AnalogComponent)

A = sympy.solve(N1.V - N3.V - V1.VSupply)

print (A, type(A[0]), type(int(A[0])))



