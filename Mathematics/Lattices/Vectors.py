'''
Given a three dimensional vector space defined over the reals, where v = (2,6,3), w = (1,0,0) and u = (7,7,2), calculate 3*(2*v - w) ∙ 2*u.
'''
import numpy as np

v=[2,6,3]
w=[1,0,0]
u=[7,7,2]

v=np.dot(2, v)
v=np.subtract(v,w)
u=np.dot(2,u)
v=np.dot(3,v)

print(np.dot(v,u))

#or using sage
#sage: v = vector([2,6,3])
#sage: w = vector([1,0,0])
#sage: u = vector([7,7,2])
#sage: 3*(2*v-w)*2*u