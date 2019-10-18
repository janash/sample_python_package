"""
molecool
A Python package for analyzingnd visualizing xyz files. For MolSSI Workshop.
"""

# Add imports here
from .measure import calculate_angle, calculate_distance
from .molecule import build_bond_list, calculate_center_of_mass, calculate_molecular_mass
from .visualize import draw_molecule, bond_histogram
import molecool.io

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
