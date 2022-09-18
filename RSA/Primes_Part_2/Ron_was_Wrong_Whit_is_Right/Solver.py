'''
Some of the public keys have a factor in common, so if we take the gcd of them, we will be able to factor the moduli and break the encryption.
'''
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from math import gcd

path=r"C:\Users\lukic\Desktop\CryptoHack\RSA\Primes_Part_2\Ron_was_Wrong_Whit_is_Right\keys_and_messages\\"

def getN(n):
    with open(path+str(n)+'.pem') as f:
        key = RSA.importKey(f.read())
    return key.n, key.e

N, e = getN(21)

for i in range(1, 50):
    Ni, _ = getN(i)
    if 1 < gcd(N, Ni) < N:
        p = gcd(N, Ni)
        q = N//p
        phi = (p-1)*(q-1)
        d = pow(e, -1, phi)
        pvt = RSA.construct((N, e, d))
        break

cipher = PKCS1_OAEP.new(pvt)
for i in range(1, 50):
    with open(path+str(i)+'.ciphertext') as f:
        enc_flag = bytes.fromhex(f.read())
        try:
            flag = cipher.decrypt(enc_flag)
            print(flag)
        except:
            pass

