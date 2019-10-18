"""
Testing for molecule module
"""

import molecool
import pytest
import sys
import os

import numpy as np

current_location = os.path.dirname(__file__)

def test_read_xyz():
    xyz_file = os.path.join(current_location, '..', 'data', 'xyz', 'water.xyz')
    symbols, coordinates = molecool.io.open_xyz(xyz_file)

    assert len(symbols) == 3
    assert len(coordinates) == 3
    assert np.array_equal(np.array([0.000000, -0.007156, 0.965491]), coordinates[0])

def test_write_xyz(tmp_path):
    """Test which writes a temporary file using pytest tmp_path function"""
    
    symbols = ["H", "O", "H"]
    coordinates = np.array([[0.0,0.0,0.0], [0.0,1.0,0.0], [1.0, 0.0, 0.0]])

    expected_text = '''3
XYZ file
H\t0.0\t0.0\t0.0
O\t0.0\t1.0\t0.0
H\t1.0\t0.0\t0.0
'''.format()

    temp_file = tmp_path / ".txt"

    location = str(temp_file)
    molecool.io.write_xyz(location, symbols, coordinates)

    written_text = temp_file.read_text()

    assert expected_text == written_text

