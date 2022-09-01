import base64
import codecs
import json
from pwn import * 
import json
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(100):
    recieved = json_recv()
    encoding = recieved['type']
    encoded = recieved['encoded']

    if encoding == "base64":
        decoded = base64.b64decode(encoded).decode()
    elif encoding == "hex":
        decoded = bytes.fromhex(encoded).decode()
    elif encoding == "rot13":
        decoded = codecs.decode(encoded, "rot13")
    elif encoding == "bigint":
        decoded = long_to_bytes(int(encoded, 16)).decode()
    elif encoding == "utf-8":
        decoded = "".join(chr(o) for o in encoded)

    print(f"{i + 1}) {encoding}:")
    print(f"{encoded} ---> {decoded}\n")

    json_send(
        {"decoded": decoded}
    )
    
recieved = json_recv()