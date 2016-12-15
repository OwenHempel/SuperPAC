#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5

import AnalogComponent
import Node
import Supply
import sympy
import Analyzer

R1 = AnalogComponent.Resistor(8)
R2 = AnalogComponent.Resistor(8)
C2 = AnalogComponent.Capacitor(1000)
C1 = AnalogComponent.Capacitor(1000)

V1 = Supply.DCVoltageSupply(12)




N1 = Node.Node(sympy.Symbol('V1'))
N2 = Node.Node(sympy.Symbol('V2'))
N3 = Node.Node(sympy.Symbol('V3'))

R1.connect(N1)
R1.connect(N2)

R2.connect(N2)
R2.connect(N3)

V1.connect(N1)
V1.connect(N3)
N1.ground()

VN2 = sympy.solve(N1.V - N3.V - V1.VSupply)
ImpR = sympy.sympify(R1.Impedance)
ImpC = sympy.sympify(C1.Impedance)
ImpR2 = sympy.sympify(R2.Impedance)


path = [C1, C2]

print (Analyzer.SeriesEquivalent(path), Analyzer.ParallelEquivalent(path))

print (N1.V, N2.V, N3.V)

int('d')




