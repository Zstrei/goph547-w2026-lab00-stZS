import sys
print(sys.path)


import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image 

from goph547lab00.arrays import (
    square_ones,
)


def arrays():

    A_np = np.ones((3, 3))
    A = square_ones(3)
    print(f'A_np:\n{A_np}')
    print(f"A:\n{A}")
    print()

    #Question B1
    C = np.ones((3, 5))
    print(f"Question B1: (3, 5) array of ones \n{C}")