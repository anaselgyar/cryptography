from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from os import urandom

plaintext = pad(b"cryptoisfun", 16)

# key derivation
passphrase = b"itsasecret"
salt = urandom(16) # 128 bits
key = PBKDF2(passphrase, salt, 16, 1000) 

# encryption
iv = urandom(16) # 128 bits
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = b64encode(cipher.encrypt(plaintext))

# decryption
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = cipher.decrypt(b64decode(ciphertext))


print(f"encrypted: {ciphertext}")
print(f"decrypted: {decrypted}")