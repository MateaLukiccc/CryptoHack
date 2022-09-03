'''Sizes and basis
size of a vector is equal to adding all coordinate squares and taking sqrt
'''

import numpy as np

v=np.array([4,6,2,5])
print(np.linalg.norm(v))  #or sqrt(dot(v,v))