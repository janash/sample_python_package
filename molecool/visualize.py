"""
Functions for visualization of molecules
"""
import numpy as np
import matplotlib.pyplot as plt

from .atom_data import atom_colors

def draw_molecule(coordinates, symbols, draw_bonds=None, save_location=None, dpi=300):
    """Draw a picture of a molecule.

    Parameters
    ----------
    coordinates : np.ndarray
        The coordinates of the molecule.
    symbols : list
        The element of each atom in the molecule.
    draw_bonds : dict, (optional)
        Bonds to draw. Bonds should be indicated in a dictionary where the indices 
        of bonded atoms are given as the keys of the dictionary. The default is None -
        no bonds are drawn.
    save_location : str, (optional)
        The location to save the image
    dpi : int, (optional)
        The resolution of the saved image

    Returns
    -------
    ax : matplotlib axis
        The axis of the plot.

    """
    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Get colors - based on atom name
    colors = []
    for atom in symbols:
        colors.append(atom_colors[atom])
    
    size = np.array(plt.rcParams['lines.markersize'] ** 2)*200/(len(coordinates))

    ax.scatter(coordinates[:,0], coordinates[:,1], coordinates[:,2], marker="o",
               edgecolors='k', facecolors=colors, alpha=1, s=size)
    
    # Draw bonds
    if draw_bonds:
        for atoms, bond_length in draw_bonds.items():
            atom1 = atoms[0]
            atom2 = atoms[1]
            
            ax.plot(coordinates[[atom1,atom2], 0], coordinates[[atom1,atom2], 1],
                    coordinates[[atom1,atom2], 2], color='k')
            
    plt.axis('square')
    
    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi, graph_min=0, graph_max=2)
    
    return ax

def bond_histogram(bond_list, save_location=None, dpi=300, graph_min=0, graph_max=2):
    """Draw a histogram of bonds lengths in a molecule.

    Parameters
    ---------
    bond_list : dict
        Bonds to draw. Bonds should be indicated in a dictionary where the indices 
        of bonded atoms are given as the keys of the dictionary. The default is None -
        no bonds are drawn.
    save_location : str, (optional)
        The location to save the image
    dpi : int, (optional)
        The resolution of the saved image
    """
    
    lengths = []
    for atoms, bond_length in bond_list.items():
        lengths.append(bond_length)
    
    bins = np.linspace(graph_min, graph_max)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    plt.xlabel('Bond Length (angstrom)')
    plt.ylabel('Number of Bonds')
    
    
    ax.hist(lengths, bins=bins)
    
    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi)
    
    return ax