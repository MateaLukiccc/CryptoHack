'''
The Elliptic Curve Discrete Logarithm Problem (ECDLP) is the problem of finding an integer n such that Q = nP.
Using the curve, prime and generator:

E: Y2 = X3 + 497 X + 1768, p: 9739, G: (1804,5368)

Calculate the shared secret after Alice sends you QA = (815, 3190), with your secret integer nB = 1829.
'''

from Point_Addition import EC,ECDH,Coord
import hashlib

if __name__=="__main__":
    ec=EC(497,1768,9739)
    G=Coord(1804,5368)
    ecdh=ECDH(ec,G)
    
    bpriv=1829                  #nb
    apub=Coord(815,3190)        #Qa
    
    print(ecdh.secret(bpriv,apub))
    x=b'7929'
    
    print(hashlib.sha1(x).hexdigest())
