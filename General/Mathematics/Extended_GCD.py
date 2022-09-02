'''
The extended Euclidean algorithm is an efficient way to find integers u,v such that

a * u + b * v = gcd(a,b)

Using the two primes p = 26513, q = 32321, find the integers u,v such that

p * u + q * v = gcd(p,q)
'''


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

print (egcd(26513,32321))
