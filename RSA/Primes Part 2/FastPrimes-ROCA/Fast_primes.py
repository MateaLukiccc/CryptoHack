from binascii import unhexlify
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes

f = open(r'/home/matea/Downloads/key_17a08b7040db46308f8b9a19894f9f95.pem','r')
key = RSA.importKey(f.read())

print(key.n,key.e)

#after we get n and e we run the scrypt in notebook with command %run roca_attack.py and we get the flag