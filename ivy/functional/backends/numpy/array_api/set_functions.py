# global
import numpy as np
from typing import Tuple
from collections import namedtuple

def unique_counts(x: np.array) \
                -> Tuple[np.array, np.array]:
    uc = namedtuple('uc', ['values', 'counts'])
    v, c = np.unique(x, return_counts=True)
    return uc(v, c)