'''
The following integers: 588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237 are successive large powers of an integer x, modulo a three digit prime p.
'''

#since p is 3 digits p<1000 and biggest number in sequence is 851 so
#851<p<1000

powers=[588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]

#since x^n=588 mod p
#we have that x^(n+1)=665 mod p => 
#588*x=665 mod p
#665*x=216 mod p
#216*x=113 mod p

#So we use sage to solve system of modular equations

'''
primes = []
for i in range(851, 999):
  if is_prime(i):
    primes.append(i)
        
x = var('x')
for p in primes:
  print(p, solve_mod([ 588*x == 665, 665*x == 216, 216*x == 113 ], p))
'''