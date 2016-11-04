#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5

import AnalogComponent
import Node

R1 = AnalogComponent.Resistor(8)
R2 = AnalogComponent.Resistor(16)

print(R1.R)

N1 = Node.Node()
N2 = Node.Node()
N3 = Node.Node()

R1.connect(N1)
R1.connect(N1)
R1.connect(N2)
R1.disconnect(N1)
R1.disconnect(N2)
R1.disconnect(N1)

R1.connect(N1)
R1.connect(N2)
R2.connect(N2)
R2.connect(N3)

