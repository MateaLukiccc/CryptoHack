'''
We can encrypt in CBC and decrypt in EBC so we need to undestand different modes in AES

1)EBC just divides plaintext in 16 sized blockes and encrypts it that way
2)CBC before the encryption it XORs every block with previous and first with IV

So since ct is 96 hex digits that is 48 bytes and we have 3 16 byte blocks B1 B2 B3
CBC encryption:
C1=E(IV ^ P1)
C2=E(C1 ^ P2)
C3=E(C2 ^ P3)

Since we have decryption option with EBC it stands that:

O1=D(C1)=D(E(IV ^ B1))=IV ^ P1
O2=C1 ^ P2
O3=C2 ^ P3

so we can look at C1 as IV and make it like we know IV so our task becomes

ciphertext=IV+C1+C2 and since we can decrypt C1 and C2 we have O1=IV ^ P1 and O2= C1 ^ P2 =>P1=IV ^ O1 and we can get P2 so we have the flag
'''

def xor(a,b):
    a = bytes.fromhex(a)
    b = bytes.fromhex(b)
    return bytes(i ^ j for i,j in zip(a,b))


ct="ce801a6ee42f65686a0b5b406e70fb7d26afc3a4146782049bc453d577d1effa5650ee2fca019041faef892085da7e1a"


import textwrap
iv=textwrap.wrap(ct, len(ct)//3)[0]
ciphertext_block1=textwrap.wrap(ct, len(ct)//3)[1]
ciphertext_block2=textwrap.wrap(ct, len(ct)//3)[2] 


decrypted_block2="799bb5942503dd35ac9b72f456f0ce87"
plaintext_block2 = xor(decrypted_block2,ciphertext_block1)

decrypted_block1="adf2631e90401e5b096904751b139048"
plaintext_block1 = xor(decrypted_block1,iv)

print(plaintext_block1+plaintext_block2)


