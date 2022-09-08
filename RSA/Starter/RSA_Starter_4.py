'''
Given the two primes:
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
and the exponent:
e = 65537
What is the private key d?
'''
from Crypto.Util.number import inverse

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

phi=(p-1)*(q-1)

d=inverse(e,phi)  #or pow(e,-1,n)

print(d)