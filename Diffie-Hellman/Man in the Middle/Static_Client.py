Alice={"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0xddf0926444085b042f503e09b718a34a81f92f4ae6704ad70e5afd3d97b447cef3c854d49a0b6ab599a564bdf8fb1d06bf250ee65ba9519249482d747aebc0572cf0329dd136b0acea24409d14aaf93b075472bc92c29c6368dac46f251201a182a4f82b0bccbabfd70c188ca72f68032d7d1ccc0488b7669971d9597fe415ac117bc8ad240ecbea01593e0ae2b5de4364143368f471e28bea47ef9802d49d677a650bafd6d2736d96335aced79f77fa48601c5d7e6d866bfa1b0a3a91875c20"}
Bob={"B": "0x8d79b69390f639501d81bdce911ec9defb0e93d421c02958c8c8dd4e245e61ae861ef9d32aa85dfec628d4046c403199297d6e17f0c9555137b5e8555eb941e8dcfd2fe5e68eecffeb66c6b0de91eb8cf2fd0c0f3f47e0c89779276fa7138e138793020c6b8f834be20a16237900c108f23f872a5f693ca3f93c3fd5a853dfd69518eb4bab9ac2a004d3a11fb21307149e8f2e1d8e1d7c85d604aa0bee335eade60f191f74ee165cd4baa067b96385aa89cbc7722e7426522381fc94ebfa8ef0"}
Alice2= {"iv": "56489104d7e068188c961c7bde7e0f88", "encrypted": "4eb1ba4b4f1ca917215d24b8f427175c33570f2630ee710d9fed4aedaaa3cefc"}


Alice3={"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0xddf0926444085b042f503e09b718a34a81f92f4ae6704ad70e5afd3d97b447cef3c854d49a0b6ab599a564bdf8fb1d06bf250ee65ba9519249482d747aebc0572cf0329dd136b0acea24409d14aaf93b075472bc92c29c6368dac46f251201a182a4f82b0bccbabfd70c188ca72f68032d7d1ccc0488b7669971d9597fe415ac117bc8ad240ecbea01593e0ae2b5de4364143368f471e28bea47ef9802d49d677a650bafd6d2736d96335aced79f77fa48601c5d7e6d866bfa1b0a3a91875c20", "A": "0x2b1ef810e424ccc50bb7cf0cc9b7acb87dd7f1e5dd5a9938a703cbe2e8fc5938fc0ad08a169c249a01b864dab5cb137a9d161d304987a2c1c756da0b559a9a889a0d3771b0832f662f9045e2e9e82d6761f62f63c6eaccfbc26f64cdd1a4c5ea"}


Bob={"B": "0xd207657a22e60b0ade33ff06e96c4959ba8f5108bb457be81478327016f5d0be5abd75e72dcfdd2128f5beb6397bea6e85ea1245429a911ecc7ed1f98acaeddd71cb26072067e5bb5f2b34526463693b0481077d941d8bfb953dafac9cf5946c49b32e2cbb60fd5ada602bf49e4e41509cb1ec88ec4ae0fc7f826ae2fc98220f9418b2bc7deefa3f00468efeaadb8dda36fc202ddf7e5d9228c7f2f0644bc65168a2d87be51c91e44513aecd52a5904a9f13f15ec6dfb79b57152acd4f39726a"}
Bob2= {"iv": "c4611f65ceba6f52abbc947a2b47de38", "encrypted": "d1e3573e768f6087306c46a1f41e613641a59a7f9fe2cf6a73b5ad744538493fae82d2648b09231881844549fa751e6da734d41ebe6dce8308cc28b3668597f486e76b76f4890dc2f2a8ec72c8937155"}


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
        return plaintext
##################################################################################################################################################################




shared_secret = int(Bob["B"],16)
iv = Alice2['iv']
ciphertext = Alice2['encrypted']

print(decrypt_flag(shared_secret, iv, ciphertext))
