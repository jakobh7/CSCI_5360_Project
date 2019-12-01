#Code inspired by https://gist.github.com/sanjay555/c2d0aa461edf8fd34c9493c82847524f

from Cryptodome.Cipher import AES
import base64
import os

class AESEncrypt(object):

    def __init__(self, BLOCK_SIZE, PADDING):
        # the block size for the cipher object; must be 16, 24, or 32 for AES
        self.BLOCK_SIZE = BLOCK_SIZE

        # the character used for padding--with a block cipher such as AES, the value
        # you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
        # used to ensure that your value is always a multiple of BLOCK_SIZE
        self.PADDING = PADDING

        # generate a random secret key
        self.secret = os.urandom(BLOCK_SIZE)

    # one-liner to sufficiently pad the text to be encrypted
    def pad(self, s):
        pad = (s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * self.PADDING).encode('utf-8')
        return pad

    # functions to encrypt/encode and decrypt/decode a string
    # encrypt with AES, encode with base64
    def encode(self, input):
        # create a cipher object using the secret
        cipher = AES.new(self.secret, AES.MODE_ECB)
        # encode a string
        encryptData = base64.b64encode(cipher.encrypt(self.pad(input)))
        return encryptData

    def decode(self, encryptedString):
        cipher = AES.new(self.secret, AES.MODE_ECB)
        decryptData = str(cipher.decrypt(base64.b64decode(encryptedString)), 'utf-8').rstrip(self.PADDING)
        return decryptData

if __name__ == '__main__':
    crypto = AESEncrypt(32, '{')
    # print(crypto.BLOCK_SIZE)
    encrypted = crypto.encode("HOW MUCH MORE CAN I ENCODE???")
    print(base64.b64decode(encrypted), 'utf-8')
    decrypted = crypto.decode(encrypted)
    print(decrypted)
