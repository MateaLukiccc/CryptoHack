'''
We've looked at multiplication and division in modular arithmetic, but what does it mean to take the square root modulo an integer?
As a = 11, a^2 = 5, we say the square root of 5 is 11.

For the elements of F*p, not every element has a square root. In fact, what we find is that for roughly one half of the elements of Fp*, there is no square root.

We say that an integer x is a Quadratic Residue if there exists an a such that a^2 = x mod p. If there is no such solution, then the integer is a Quadratic Non-Residue.

In the below list there are two non-quadratic residues and one quadratic residue.
Find the quadratic residue and then calculate its square root. Of the two possible roots, submit the smaller one as the flag.
'''

p = 29
ints = [14, 6, 11]

q_residue_root=[]
q_residue=0
for x in ints:
    for i in range(29):
        if i**2 % p == x:
            q_residue=x
            q_residue_root.append(i)             #if i^2=x mod p then modular sqrt(x)=i
            
                   
print(q_residue,q_residue_root) 
