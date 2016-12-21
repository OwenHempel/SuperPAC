SuperPAC Circuit Solutions
==========================

Basic Representations
---------------------

Analog Circuit Solution
^^^^^^^^^^^^^^^^^^^^^^^

SuperPAC uses SymPy to create equations at given nodes. Each node has a number of paths that connect it to the other nodes. Along each path will be a series of Components. Elements each have equations for voltage and current. By iteratively calculating each node's Voltage and Current, equations can be generated which can be solved by SymPy's solver.



Domains
-------

Frequency Domain
^^^^^^^^^^^^^^^^

Frequency-domain representations of circuits are often useful as an analytic tool. SuperPAC has the ability to generate frequency domain representations of circuits, and present frequency response.

Time Domain
^^^^^^^^^^^

Of course, SuperPAC has the ability to show time domain as well. Arbitrary time intervals across a user-set range make it easy to see how a circuit would respond over a period of time. 