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
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])
    return symbols, coordinates

def test_build_bond_list_default(test_molecule):
    symbols, coordinates = test_molecule

    bonds = molecool.build_bond_list(coordinates)

    assert len(bonds) == 4

    for atoms, bonds in bonds.items():
        assert bonds == 1.4

def test_molecular_mass(test_molecule):
    symbols, coordiantes = test_molecule
    
    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = molecool.atom_data.atom_weights['C'] + molecool.atom_data.atom_weights['H'] +\
         molecool.atom_data.atom_weights['H'] + molecool.atom_data.atom_weights['H'] + molecool.atom_data.atom_weights['H']

    assert actual_mass == calculated_mass

def test_build_bond_list_failure():
    coordinates = np.array([])
    
    with pytest.raises(ValueError):
        molecool.build_bond_list(coordinates)

def test_center_of_mass(test_molecule):
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])

    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1,1,1])
    
    assert np.array_equal(center_of_mass, expected_center)