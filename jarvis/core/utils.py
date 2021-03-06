"""Set of useful utility functions."""

from collections import OrderedDict
from collections import defaultdict
import random
import numpy as np
import math


def get_counts(array=["W", "W", "Mo", "Mo", "S", "S"]):
    """
    Get number of unique elements and their counts.

    Uses OrderedDict.

    Args:
         array of elements

    Returns:
         ordereddict, e.g.OrderedDict([('W', 2), ('Mo', 2), ('S', 2)])
    """
    uniqe_els = []
    for i in array:
        if i not in uniqe_els:
            uniqe_els.append(i)
    info = OrderedDict()
    for i in uniqe_els:
        info.setdefault(i, 0)
    for i in array:
        info[i] += 1
    return info


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a % b
    return a


def ext_gcd(a, b):
    """GCD module from ase."""
    if b == 0:
        return 1, 0
    elif a % b == 0:
        return 0, 1
    else:
        x, y = ext_gcd(b, a % b)
        return y, x - y * (a // b)


def rand_select(x=[]):
    """Select randomly with index info."""
    info = {}
    for i, ii in enumerate(x):
        info.setdefault(ii, []).append(i)
    selected = {}
    for i, j in info.items():
        chosen = random.choice(j)
        selected.setdefault(i, chosen)
    return selected


def rec_dict():
    """Make a recursion dictionary."""
    return defaultdict(rec_dict)


def random_colors(number_of_colors=110):
    """Generate random colors for atom coloring."""
    colors = [
        "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
        for i in range(number_of_colors)
    ]
    color_dict = {}
    for i, ii in enumerate(colors):
        color_dict[i] = ii
    return color_dict


def get_angle(
    a=np.array([1, 2, 3]), b=np.array([4, 5, 6]), c=np.array([7, 8, 9])
):
    """Get angle between three vectors."""
    # theta = argcos(x.y/(|x||y|))
    cos = np.dot((a - b), (c - b)) / (
        np.linalg.norm((a - b)) * np.linalg.norm((c - b))
    )
    if cos <= -1.0:
        cos = cos + 0.000001
    if cos >= 1.0:
        cos = cos - 0.000001
    angle = math.degrees(math.acos(cos))
    return angle


# color_dict=random_colors()
