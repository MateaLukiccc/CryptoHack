from Crypto.Cipher import AES
import hashlib

ct="c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"

def decrypt(ciphertext, key):
    ciphertext = bytes.fromhex(ciphertext)
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return decrypted

f=open(r"C:\Users\lukic\Desktop\CryptoHack\Symmetric Ciphers\Symmetric Starter\words.txt","r")
words = [w.strip() for w in f.readlines()]


for i in words:
    KEY = hashlib.md5(i.encode()).digest()
    plain=decrypt(ct,KEY)
    if b'crypto' in plain:
        print(plain)
        
        
        
