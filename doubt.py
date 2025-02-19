import numpy as np
import random
from scipy import *
from pylab import *

# Generate a 3x3 matrix with random numbers from 0 to 6
matrix = np.random.randint(0, 7, size=(3, 3))

print(matrix)
print(eig((matrix)))
