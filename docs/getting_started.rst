Getting Started
===============

molecool is currently under development, and can not yet be installed from PyPI
or conda. 

Installation
------------
**These instructions assume you have the python package manager `conda` installed.**

To install molecool, navigate to the `GitHub <https://www.github.com/YOUR_GITHUB_USERNAME/molecool>`_ and clone the repository to your computer.

To do a developmental install, type

``$ pip install -e .``

Dependencies
^^^^^^^^^^^^
You need to install `numpy` and `matplotlib`.

You can now use and develop this package!

Usage
-------
Once installed, you can use the package. This example draws a benzene molecule from an xyz file.::

    import molecool
    
    benzene_symbols, benzene_coords = molecool.open_xyz('benzene.xyz')
    benzene_bonds = molecool.build_bond_list(benzene_coords)
    molecool.draw_molecule(benzene_coords, benzene_symbols, draw_bonds=benzene_bonds)

