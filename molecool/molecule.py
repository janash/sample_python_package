"""
Functions for calculating molecule properties.
"""

from .measure import calculate_distance
from .atom_data import atom_weights

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    """Calculate bonds in a molecule base on a distance criteria.

    The pairwise distance between atoms is computed. If it is in the range 
    `min_bond` to `max_bond`, the atoms are counted as bonded.

    Parameters
    ----------
    coordinates : array-like
        The coordinates of the atoms.
    max_bond : float (optional)
        The maximum distance for two points to be considered bonded. The default
        is 1.5
    min_bond : float (optional)
        The minimum distance for two points to be considered bonded. The default
        is 0.
    
    Returns
    -------
    bonds : dict
        A dictionary where the keys are tuples of the bonded atom indices, and the
        associated values are the bond length.

    """
    
    # Find the bonds in a molecule
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds

def calculate_molecular_mass(symbols):
    """Calculate the mass of a molecule.
    
    Parameters
    ----------
    symbols : list
        A list of elements.
    
    Returns
    -------
    mass : float
        The mass of the molecule
    """

    mass = 0
    for atom in symbols:
        mass += atom_weights[atom]
    
    return mass

# Using the atomic_weights dictionary, write a function which calculates the center of mass of a molecule.
def calculate_center_of_mass(symbols, coordinates):
    """Calculate the center of mass of a molecule.
    
    The center of mass is weighted by each atom's weight.
    
    Parameters
    ----------
    symbols: list
        A list of elements for the molecule
    coordinates : np.ndarray
        The coordinates of the molecule.
    
    Returns
    -------
    center_of_mass: np.ndarray
        The center of mass of the molecule.

    Notes
    -----
    The center of mass is calculated with the formula
    
    .. math:: \vec{R}=\frac{1}{M} \\sum_{i=1}^{n} m_{i}\vec{r_{}i}
    """
    
    total_mass = calculate_molecular_mass(symbols)
    
    mass_array = np.zeros([len(symbols), 1])
    
    for i in range(len(symbols)):
        mass_array[i] = atomic_weights[symbols[i]]
    
    center_of_mass = sum(coordinates * mass_array) / total_mass
    
    return center_of_mass
    