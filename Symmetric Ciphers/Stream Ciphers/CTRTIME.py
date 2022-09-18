'''
Smallest amount of memory will be occupied if we compress already used chars or in our case flag chars 
so we will compare all returned strings and when we get smaller one we know we used correct char that
belongs in flag
source: https://en.wikipedia.org/wiki/CRIME
'''

import requests, sys

solution = "crypto{"
chars = 'ABCDEFGHIJKLMNOPQRTSUVWXYZ0123456789_abcdefghijklmnopqrstuvwxyz}'
invalid_char = ';'

while True:
    p = (solution + invalid_char) * 2
    r = requests.get("https://aes.cryptohack.org/ctrime/encrypt/" + p.encode('ascii').hex()).json()
    sample = len(r['ciphertext'])
    for c in chars:
        r = requests.get("https://aes.cryptohack.org/ctrime/encrypt/" + ((solution + c) * 2).encode('ascii').hex()).json()
        if len(r['ciphertext']) < sample:
            solution += c
            print(solution)
            if c == "}":
                print("Solution Found!", solution)
                sys.exit()
            break