"""
This module is for functions which perform measurements.
"""

import numpy as np

def calculate_distance(rA, rB):
    """Calculate the distance between two points.

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.
    
    Returns
    -------
    distance : float
        The distance between the two points.
    """
    dist_vec = (rA - rB)
    distance = np.linalg.norm(dist_vec)
    return distance

def calculate_angle(rA, rB, rC, degrees=False):
    """Calculate the angle between three points.

    Parameters
    ----------
    rA, rB, rC : np.ndarray
        The coordinates of each point
    degrees : bool , optional
        Return unit of the calculated answer. Default is in radians.

    Returns
    -------
    angle : float
        The angle measurement for the three points.
    """
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta
