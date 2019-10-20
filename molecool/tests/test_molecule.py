"""
Testing for molecule module
"""

import molecool
import pytest
import sys

import numpy as np
import os

@pytest.fixture
def test_molecule():
    symbols = np.array(['C', 'H', 'H'])
    coordinates = np.array([[0,0,0], [1.4,0,0], [0, 1.4, 0], [0, 0, 1.4]])
    return symbols, coordinates

def test_build_bond_list_default(test_molecule):
    symbols, coordinates = test_molecule

    bonds = molecool.build_bond_list(coordinates)

    assert len(bonds) == 3

    for atoms, bonds in bonds.items():
        assert bonds == 1.4

def test_build_bond_list_failure():
    coordinates = np.array([])
    
    with pytest.raises(ValueError):
        molecool.build_bond_list(coordinates)