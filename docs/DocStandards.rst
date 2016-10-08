Documentation Standards
=======================

Build Engine
------------

SuperPAC documentation will be built using Sphinx. Thus, all documentation (including this guide) will be plaintext ReStructured Text (.rst) files and/or contained within the python source itself.

If you wish to write modules (And you are welcome to do so), and you want them included in the project, the modules have to be commented properly so that everybody is on the same page. 

Modules and Classes
-------------------

Code modules/classes will be rejected unless they have some key items in the docstrings. Firstly, any modules that are imported anywhere within the module should be listed under a bold heading **Imports**. Parent classes should be listed as well, and a short but clear description of the purpose of the module must be included.

`
""
**Imports:** Cream, Sugar

**Parent classes:** Pie, Pastry

**Description:** The filling is the most important part of the pie. It provides the sweet taste and moisture.
"""
`

Functions and Methods
---------------------



`
"""
Args:
	Row (list): Rule, read from the sql database 
Returns:
	Bool: noOverlap
Returns true if one of the rule limits falls between the limits of another rule OR if the rules have the same limits"""
`
	