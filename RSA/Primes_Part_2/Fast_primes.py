import random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, bytes_to_long, inverse
from gmpy2 import is_prime

f = open(r'/home/matea/Downloads/key_17a08b7040db46308f8b9a19894f9f95.pem','r')
key = RSA.importKey(f.read())

print(key.n,key.e)

#after we get n and e we run the scrypt in notebook with command %run roca_attack.py and we get the flag

p=77342270837753916396402614215980760127245056504361515489809293852222206596161
q=51894141255108267693828471848483688186015845988173648228318286999011443419469
phi=(p-1)*(q-1)
e=65537
d=pow(e,-1,phi)
c = "249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28"
c = int(c, 16)
key = RSA.construct((key.n, e, d))
cipher = PKCS1_OAEP.new(key)
message = cipher.decrypt(long_to_bytes(c))
print(message)

