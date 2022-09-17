'''
We can encrypt in CBC and decrypt in EBC so we need to undestand different modes in AES

1)EBC just divides plaintext in 16 sized blockes and encrypts it that way
2)CBC before the encryption it XORs every block with previous and first with IV

So since ct is 96 hex digits that is 48 bytes and we have 3 16 byte blocks B1 B2 B3
CBC encryption:
C1=IV
C2=E(IV ^ P1)
C3=E(C1 ^ P2)=E(E(IV ^ P1) ^ P2)

so ciphertext=IV+E(IV ^ P1)+E(E(IV ^ P1) ^ P2)

Since we have decryption option with EBC it stands that:

O1=D(IV)
O2=IV ^ P1
O3=E(IV ^ P1) ^ P2


from C1 ^ O2 we can get P1 and then P2
'''


ct="2f073a622d39e70119b32df22c9abfdf39cdef6e511b2e390e17c052bd61566fb124db243de4e629f300e8675134f3fb"

pt="a7cf3248e76adf7ab26339503a485ca74c75431259569c327ad172c759f9d4ea66f9995e607f71083948e1739c407712"

from pwn import xor

iv=ct[:32]
db1=xor(bytes.fromhex(iv),bytes.fromhex(pt[32:64]))
db2=xor(bytes.fromhex(ct[32:64]),bytes.fromhex(pt[64:]))

print(db1,db2,sep="")


#different approach
'''
def xor(a,b):
    a = bytes.fromhex(a)
    b = bytes.fromhex(b)
    return bytes(i ^ j for i,j in zip(a,b))
'''

#another way to split text 
#import textwrap
#iv=textwrap.wrap(ct, len(ct)//3)[0]