'''
Chosen plaintext attack on ECB  https://crypto.stackexchange.com/questions/42891/chosen-plaintext-attack-on-aes-in-ecb-mode
TLDR:
ciphertext consists of input+flag+pad if blocks are 16 chars long(they are 32 but for demonstration lets say 16) then we have for input A*15:
AAAAAAAAAAAAAAAc | rypto{wow}xxxxx 
so if we send A*15 +all chars and match reference block with our made up we get flag letter by letter 
'''
import requests
import string
import binascii,json

url='http://aes.cryptohack.org/ecb_oracle/encrypt/'

def hex(p):
    return (binascii.hexlify(p.encode())).decode()


flag=''
input='A'*32 #Let's assume flag length is between 16-32
k=0
while k<33:
    for i in string.ascii_letters+string.digits+'{_}':
        
        r = requests.get(url+hex(input[:-1]))                            #input is A*31
        
        ref_block=json.loads(r.text)["ciphertext"][:64] #Reference block      #we get reference bloc for A*31+?
        
        r = requests.get(url+hex(input[:-1]+flag+i))                          #we send A*31+i  because flag='' until i matches ?
        
        if json.loads(r.text)["ciphertext"][:64]==ref_block:
            flag+=i
            print("\r"+flag, flush=True, end='') #crypto{p3n6u1n5_h473_3cb}
            break
    k+=1
    input=input[:-1]