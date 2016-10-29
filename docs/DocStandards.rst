Documentation Standards
=======================

Build Engine
------------

SuperPAC documentation will be built using Sphinx. Thus, all documentation (including this guide) will be plaintext ReStructured Text (.rst) files and/or contained within the python source itself.

If you wish to write modules (And you are welcome to do so), and you want them included in the project, the modules have to be commented properly so that everybody is on the same page. 

Docstring formatting
--------------------

Remember that sphinx formatting applies in docstrings when you include them in sphinx. For a full description, refer to the sphinx documentation on docstrings

Modules and Classes
-------------------

Code modules/classes will be rejected unless they have some key items in the docstrings. Firstly, any modules that are imported anywhere within the module should be listed under a bold heading **Imports**. Parent classes should be listed as well, and a short but clear description of the purpose of the module must be included.


.. code-block:: python

  module filling:
  """
  **Imports:** Cream, Sugar

  **Parent classes:** Pie, Pastry

  **Description:** The filling is the most important part of the pie. It provides the sweet taste and moisture.
  """
  

Which will produce the following in the description of the module:

**Imports:** Cream, Sugar

**Parent classes:** Pie, Pastry

**Description:** The filling is the most important part of the pie. It provides the sweet taste and moisture.

And of course, the same applies for a sample class:

.. code-block:: python

  Class sample_class:

	'''The class for our combination temperature/humidity sensor. 

	**Methods:** 

	* :func:`htu_reset`
	* :func:`read_temperature`
	* :func:`read_humidity`

	Initialized during initialization of the main control loop. Periodic calls to the methods will be made in the main control loop.
	'''

And the output:

**Methods:** 
	
* :func:`htu_reset`
* :func:`read_temperature`
* :func:`read_humidity`

Initialized during initialization of the main control loop. Periodic calls to the methods will be made in the main control loop.
	

Functions and Methods
---------------------

Functions and methods need to have docstrings too. Again, a small description of the code, what it returns and why.

Arguments and their types, as well as returns and their types must be documented.

.. code-block:: python

  def bake(time, temp):
  '''
  Args:
	Time (list): Rule, read from the sql database 
  Returns:
  	Temp: noOverlap
  Returns true if one of the rule limits falls between the limits of another rule OR if the rules have the same limits
  '''


Which makes:

Args:
	Row (list): Rule, read from the sql database 
Returns:
	Bool: noOverlap
Returns true if one of the rule limits falls between the limits of another rule OR if the rules have the same limits
	

