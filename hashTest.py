# import hashlib
# text = "0.0.0.0"
# print(text)
# m = hashlib.md5(text.encode('utf-8'))
# print(m.hexdigest())

from Cryptodome.Cipher import AES
from base64 import *

MASTER_KEY="MDN is cool!"

def encrypt_val(clear_text):
    enc_secret = AES.new(MASTER_KEY[:32])
    tag_string = (str(clear_text) +
                  (AES.block_size -
                   len(str(clear_text)) % AES.block_size) * "\0")
    cipher_text = base64.b64encode(enc_secret.encrypt(tag_string))

    return cipher_text

def decrypt_val(cipher_text):
    dec_secret = AES.new(MASTER_KEY[:32])
    raw_decrypted = dec_secret.decrypt(base64.b64decode(cipher_text))
    clear_val = raw_decrypted.decode().rstrip("\0")
    return clear_val

if __name__ == "__main__":
    text = "Test"
    eVal = encrypt_val(text)
    dval = decrypt_val(eVal)
    print(dval)