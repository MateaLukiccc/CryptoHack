'''
In the last challenge we saw that thereis a special kind of basis called an orthogonal basis. Given a basis v1, v2, ..., vn ∈ V for a vector space,
the Gram-Schmidt algorithm calculates an orthogonal basis u1, u2, ..., un ∈ V.

To test your code, let's grab the flag. Given the following basis vectors:
v1 = (4,1,3,-1), v2 = (2,1,-3,4), v3 = (1,0,-2,7), v4 = (6, 2, 9, -5),
use the Gram-Schmidt algorithm to calculate an orthogonal basis. The flag is the float value of the second component of u4 to 5 significant figures.
'''

#Solution to the problem in sage
'''
v0 = vector([4,1,3,-1])
v1 = vector([2,1,-3,4])
v2 = vector([1,0,-2,7])
v3 = vector([6,2,9,-5])
M = Matrix([v0,v1,v2,v3])
M.gram_schmidt()
'''
#0.9161073825503355
