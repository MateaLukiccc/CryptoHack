'''
A primitive element of Fp is an element whose subgroup H = Fp, i.e., every element of Fp, can be written as g^n mod p for some integer n.
Because of this, primitive elements are sometimes called generators of the finite field.

For the finite field with p = 28151 find the smallest element g which is a primitive element of Fp
'''

from tqdm import tqdm

p=28151

lst=[k for k in range(1,p)]


for g in tqdm(range(p)):
    res=[]
    n=1
    while pow(g,n,p) not in res:
        res.append(pow(g,n,p))
        n+=1
    if set(res)==set(lst):
        print("Solution: ",g)
        break


#Sage solution:
'''
k = GF(28151, modulus="primitive")
k.gen()  # this gives a primitive element
'''