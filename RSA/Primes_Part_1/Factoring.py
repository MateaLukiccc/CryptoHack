'''
Factorise the 150-bit number 510143758735509025530880200653196460532653147 into its two constituent primes. Give the smaller one as your answer.
'''

from factordb.factordb import FactorDB

n=510143758735509025530880200653196460532653147

f=FactorDB(n)
f.connect()
print(min(f.get_factor_list()))