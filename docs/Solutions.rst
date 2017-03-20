Circuit Solutions
=================

Circuits are presented as collections of :ref:`Components` and :ref:`Nodes`. Under the hood, Circuits will iteratively replace these components in parallel and in series, until it arrives at the equivalent of all the components. At each stage of reduction, a transfer function is written to two stored matrices: The Voltage and the Current matrices. The solution equations are generated in this way to ensure no duplicate equation sets, that is to say, each equation is independent. 

With the the following steps, circuits will iteratively simplify themselves. More advanced solutions engines are in progress.

1. Reduce
---------

Circuit elements are reduced in the following order: 

1. Parallel
^^^^^^^^^^^

Each set of parallel components are reduced to a single component. This step is done first 
