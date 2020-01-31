from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def decrypt(prikey, cipher):
    f = open(prikey, 'r').read()
    key = RSA.importKey(f)
    rsa = PKCS1_OAEP.new(key)
    answer = rsa.decrypt(cipher)
    return answer

#rsakey=RSA.importKey(key)
f = open('encrypted.txt','rb').read()

print(decrypt("key.ppm",f).decode())
