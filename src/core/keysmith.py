from Crypto import Random
from Crypto.Cipher import AES

# https://pycryptodome.readthedocs.io/en/latest/src/cipher/cipher.html

class aescbc():

    def __init__(self, key):
        self.crypto = AES.new(key, AES.MODE_CBC, b'1234567890123456')

    def encrypt(self, data):
        return self.crypto.encrypt(data)

    def decrypt(self, enc):
        return self.crypto.decrypt(enc)

# import keysmith as k
# a = k.aescbc(b'adsfasdfasdfasdf')
# tmp = a.encrypt(b'asdfsadf00000000')
# b = k.aescbc(b'adsfasdfasdfasdf')
# tmp2 = b.decrypt(tmp)