'''
Bit flipping attack on CBC

we have a cookie admin=False;expiry={expires_at} that we want to change to admin=True;expiry={expires_at}
and we have iv that with our original cookie(False) gives us the right ciphertext
So now we need to make new iv2 that with our new cookie(true) gives the same ciphertext
How?
Well since CBC encryption starts with IV ^ Block1 we can change block1 from admin=False;expi (16 bytes long)
to admin=True;;expi so that we basically swap False with True; and from  
IV ^ Block1 = IV2 ^ NewBlock we can get the IV2 => IV ^ Block1 ^ NewBlock = IV2 

'''
from pwn import xor
ciphertext="266414e2a194e2c9f090c48e11348d916506716f04439d6c5fcf15e169084a11ad74ad74e5d336951c5fdae2b4e452f9"

iv=bytes.fromhex(ciphertext[:32])

text=b'admin=False;expi'  #taking only the initial block... since that's only required
forge_text=b'admin=True;;expi'  #we put the block we want to replace old one 

xor_result=xor(iv,text)      #we want to make P1 ^ IV1 = P2 ^ IV2  => P1 ^ IV1 ^ P2 =IV2
forge_iv=xor(xor_result,forge_text).hex()

print("Our cookie is:",forge_iv+ciphertext[32:])
print("new iv is:",forge_iv)



