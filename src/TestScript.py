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
C1.connect(N1)
C1.connect(N2)

R2.connect(N2)
R2.connect(N3)

V1.connect(N1)
V1.connect(N3)

comps = [R1,R2]

N3.ground()

#print (Analyzer.SeriesEquivalent(path), Analyzer.ParallelEquivalent(path))

for C in comps:
	Analyzer.calcCurrent(C)
	Analyzer.calcVoltage(C)


print (R1.isSeries(C1))
print (R1.isSeries(R2))
print (R1.isParallel(C1))
print (R1.isParallel(R2))






