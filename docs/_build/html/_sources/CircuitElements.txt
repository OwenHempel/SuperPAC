Circuit Elements
================

Circuit Elements are defined here as any component you can place in your circuit.

Components
----------

Components is the high level class that all (Analog and digital) component inherit. It only defines behaviours that all components share, namely connecting and disconnecting to nodes.

.. automodule:: Component
   :members:

Analog
------

Analog Components and each subclass define the characteristics of each type of component. Using these characteristics, an analysis module can set values. No analog component should be performing any sort of calculations of its values. That way, the solving engine can be independent of the component type.

.. automodule:: AnalogComponent
	:members:

Supplies
--------

Similar to Components, supplies define types of supply. 

.. automodule:: Supply
	:members: