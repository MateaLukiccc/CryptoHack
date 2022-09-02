#Given the string "label", XOR each character with the integer 13. Convert these integers back to a string and submit the flag as crypto{new_string}.

from pwn import xor

print(xor(13,"label"))
