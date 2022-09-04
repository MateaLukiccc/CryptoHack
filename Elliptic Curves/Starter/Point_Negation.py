'''
E: Y^2 = X^3 + 497^X + 1768, p: 9739
Using the above curve, and the point P(8045,6936), find the point Q(x,y) such that P + Q = O.
'''

#since P+(-P)=O we have -P(8045,-6936)
#since we work in finite field we need to get rid of negative numbers
#p+(negative_number)=new_coordinate 

print("Q({0},{1})".format(8045,9739-6936)) 