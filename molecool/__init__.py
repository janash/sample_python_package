"""
molecool
A Python package for analyzingnd visualizing xyz files. For MolSSI Workshop.
"""

# Add imports here
from .molecool import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
