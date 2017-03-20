Circuit Solutions
=================

Circuits are presented as collections of :ref:`Components` and :ref:`Nodes`. Under the hood, Circuits will iteratively replace these components in parallel and in series, until it arrives at the equivalent of all the components. At each stage of reduction, a transfer function is written to two stored matrices: The Voltage and the Current matrices. The solution equations are generated in this way to ensure no duplicate equation sets, that is to say, each equation is independent. 

With the the following steps, circuits will iteratively simplify themselves. More advanced solutions engines are in progress.

1. Reduce
---------

Circuit elements are reduced in the following order: 

A. Parallel
^^^^^^^^^^^

Each set of parallel components are reduced to a single component. The reason for this order is that a component in series with two components in parallel would cause an error. Consider:

Component A is in series with Component B and C, which are in parallel.

A series replacement would replace components A and B with an equivalent component, AB. However, C is now left alone and will not be considered.

B. Series
^^^^^^^^^

With inner parallel components reduced, there will be components in series. Now, a series reduction will collapse those components--

C. Repeat
^^^^^^^^^


