'''
Attack on CBC when IV=KEY
if key=iv we get deterministic encryption scheme that we can easily exploit 
since
C0=E(IV ^ P0)
C1=E(C0 ^ P1)
C2=E(C1 ^ P2)
we can now change C0 and C2 since scheme is deterministic
C'0=C0
C1=0
C'1=C0
and we have
P0=IV ^ D(C'0)
P1=C'0 ^ D(0)
P2=0 ^ D(C'0)
=> P0 ^ P2 => IV
'''

ct1="a07e843ee77b6b0e05431e89ddc239348ad4a5547839122d819d1bfb76ec68c904bc07c9067e81c2f9cc8cbd64b258c6" #aaaa...a000000..0

c0=ct1[:32]
c1=ct1[32:64]
c2=ct1[64:]

print(c0,c1,c2)

cp0=c0
cp1='0'*32
cp2=c0

print(cp0,cp1,cp2,sep="")

pt="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc15da8581f9128a168dbf89ec92b89f50fecef7ef023cfe07154ea9831e0634"
p0=pt[:32]
p1=pt[32:64]
p2=pt[64:]


def hex_xor(s1, s2):
    a = bytes.fromhex(s1)
    b = bytes.fromhex(s2)
    result = bytes([b1 ^ b2 for b1, b2 in zip(a,b)])
    return result.hex()

print(hex_xor(p0,p2))




