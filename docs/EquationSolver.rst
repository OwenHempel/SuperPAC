SuperPAC Circuit Solutions
==========================

Basic Representations
---------------------

SuperPAC uses SymPy to create equations at given nodes. Each node has a number of :ref:`paths` that connect it to the other nodes. Along each path will be a series of :ref:`elements`. Elements each have equations for voltage and current. By calculating each node in terms of the reference node, voltage at an arbitrary point can be calculated. 

Domains
-------

Frequency Domain
^^^^^^^^^^^^^^^^

Frequency-domain representations of circuits are often useful as an analytic tool. SuperPAC has the ability to generate frequency domain representations of circuits, and present frequency response.

Time Domain
^^^^^^^^^^^

Of course, SuperPAC has the ability to show time domain as well. Arbitrary time intervals across a user-set range make it easy to see how a circuit would respond over a period of time. 