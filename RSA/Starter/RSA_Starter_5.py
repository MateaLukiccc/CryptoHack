'''
N = 882564595536224140639625987659416029426239230804614613279163
e = 65537
Use the private key that you found for these parameters in the previous challenge to decrypt this ciphertext:
c = 77578995801157823671636298847186723593814843845525223303932
'''
from factordb.factordb import FactorDB
from Crypto.Util.number import inverse

N = 882564595536224140639625987659416029426239230804614613279163
e = 65537
c = 77578995801157823671636298847186723593814843845525223303932

f=FactorDB(N)
f.connect()
p=f.get_factor_list()[0]
q=f.get_factor_list()[1]

phi=(p-1)*(q-1)
n=p*q

d=inverse(e,phi)

m=pow(c,d,n)

print(m)




