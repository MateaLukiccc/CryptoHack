#Intercepted from Alice: 
alice={
    
    "p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff",
    "g": "0x02",
    "A": "0xcb5a051d4ffa048b5a25f9b09411e6a913c8d3d40dbf738923dda719a578b5280ff653e903402f2cd31c92247147e7b07f8f6c8ab8beb8f9332ab0c2c6a600d31053941bcd38b1f79084ab4805a0a304bd9e8252e7aa7e724f6b9bc4946be0326a164ae5488986420b0ae21bad9d23a3c781e8db148beab6c3441ba9df9a2fbcf13f6c57cc754e1ea11f64b9b770cbd50a1350880e9f7f068617e746543ec2de0534209098fe944c5e9b379e2d85d8e175df2ba5b7db6c48c7720804c77680fd"

}

#we are asked by Bob to send Alices info if we send A=p we get that Key=A^b mod p which is 0


alice={
    "p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff",
    "g": "0x02",
    "A": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff"
}

#Intercepted from Bob: 
Bob={
    "B": "0xeec6bddbe8f728615eb50de7fbfaf1eb48b177742c17dbf4eb36089c92cd55f0b84ded89a760315cd8590a437ce4873e8b7f20c35f0a073343e9c161de2f8b2e622ec2fd2ef628600fa0c84305f4e7cfe0310f96015cc11f9a972ef56902aec46db246fd43819d0a2f33b8dab585bf6445188b39cd7f1ed8357653f452257bd2fbecac858aa392e83b856eac2f1355daafae2c65955f450394f6a0ef9cdebdd180e8135a3920cb97e6c1dcc16d352a87165ce48e1d1428d011e29e6c4a451438"
    }

#we do the same with Bobs info so that Key=0

Bob={"B": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff"}

#Intercepted from Alice: 
{"iv": "a2e50112a40a42003083016c7bf096d1", "encrypted_flag": "4117a7b00c25a6102f49b0d27bc633d04704e521d195f03b3835307410a2d28a"}


#Reused code:
########################################################################################################################################################################
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')
##################################################################################################################################################################

g= 2
p= int("ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff",16)
A= p
b= 197395083814907028991785772714920885908249341925650951555219049411298436217190605190824934787336279228785809783531814507661385111220639329358048196339626065676869119737979175531770768861808581110311903548567424039264485661330995221907803300824165469977099494284722831845653985392791480264712091293580274947132480402319812110462641143884577706335859190668240694680261160210609506891842793868297672619625924001403035676872189455767944077542198064499486164431451944
B= p
dic={"iv": "4d0f69d49565ef40f0e0eb9b1d7eeb25", "encrypted_flag": "3284948b2f82a7322e2ca0575b96b14a2dd7208547855c4c65507718f83c86bf"}


shared_secret = 0
iv = dic['iv']
ciphertext = dic['encrypted_flag']

print(decrypt_flag(shared_secret, iv, ciphertext))





