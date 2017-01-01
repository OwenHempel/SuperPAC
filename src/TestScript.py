#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5

import AnalogComponent
import Node
import Supply
import Circuit
import sympy


R1 = AnalogComponent.Resistor(8, 'R1')
R2 = AnalogComponent.Resistor(8, 'R2')
C2 = AnalogComponent.Capacitor(1000, 'C2')
C1 = AnalogComponent.Capacitor(1000, 'C1')

V1 = Supply.DCVoltageSupply(12)


Cct = Circuit.Circuit()

N1 = Node.Node(sympy.Symbol('V1'))
Cct.addNode(N1)
N2 = Node.Node(sympy.Symbol('V2'))
Cct.addNode(N2)
N3 = Node.Node(sympy.Symbol('V3'))
Cct.addNode(N3)

R1.connect(N1)
R1.connect(N2)
C1.connect(N1)
C1.connect(N2)

R2.connect(N2)
R2.connect(N3)

V1.connect(N1)
V1.connect(N3)
N3.ground()

ResS = Cct.SeriesEquivalent([R1,R2, C1])

ResP = Cct.ParallelEquivalent([R2, R1, C1,C2])

print(str(ResS) + '\n'+  str(ResP))

print(type(R1) == AnalogComponent.Resistor, type(C1))








