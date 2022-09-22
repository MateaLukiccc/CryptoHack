'''
Using JACK11, his secret has the hash value: JACK(secret) = 01011001101.

Given no other data of the JACK11 hash algorithm, how many unique secrets would you expect to hash to have (on average) a 50% chance of a collision with Jack's secret?
'''


n=11
lamb=0.75
from math import log,sqrt,ceil



t=2**((n+1)/2)*sqrt(log(1/(1-lamb)))



n=2**11
p=1
i=0
while p>0.5:
    i=i+1
    p=(((n-1)/n)**i)
    
    
#print(p,i) p is basically the probability of i people to have different birthdat=y then our target

print("We would need {0} different hashes to have 1 collision with 75% and we would need {1} hashes to collide with 1 specific hash".format(ceil(t),i))