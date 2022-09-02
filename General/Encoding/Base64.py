import base64

#Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using 64 characters.
#Take the below hex string, decode it into bytes and then encode it into Base64.

enc="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

temp=bytes.fromhex(enc)

print(base64.b64encode(temp))
