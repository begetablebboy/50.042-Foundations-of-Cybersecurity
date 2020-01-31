from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode, b64encode
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256
import argparse
import sys
from pyrsa_sq_mul import square_multiply
from pyrsa_sq_mul import unpack_bigint
from pyrsa_sq_mul import pack_bigint

""" 
    Sumedha 1002876
    For explanations of the write up, pls refer to 'hand-in' file
"""

def generate_RSA(bits=1024):
    key = RSA.generate(bits)
    public_key = key.publickey().exportKey('PEM').decode('ascii')
    private_key = key.exportKey('PEM').decode('ascii')
    with open('./sumkey.pem.pub','w') as pkfile:
        pkfile.write(public_key)

    with open('./sumkey.pem.priv','w') as skfile:
        skfile.write(private_key)

    return private_key, public_key

# Part 1: RSA without padding
def encrypt_RSA(public_key_file, message):
    pk = open(public_key_file, 'r').read()
    pkrsa = RSA.importKey(pk)
    # print('RSA import:', pkrsa)
    # print('n:', pkrsa.n)
    # print('e:', pkrsa.e)

    # a = x = message.encode
    # e = x
    # n = mod
    x = unpack_bigint(message)
    m = square_multiply(x, pkrsa.e, pkrsa.n)
    return m


def decrypt_RSA(private_key_file, cipher):
    sk = open(private_key_file, 'r').read()
    skrsa = RSA.importKey(sk)
    # print('n:', skrsa.n)
    # print('d:', skrsa.d)

    x = unpack_bigint(cipher)
    m = square_multiply(x, skrsa.d, skrsa.n)
    return m


def sign_RSA(private_key_loc, data):
    sk = open(private_key_loc, 'r').read()
    hash = SHA256.new(data).digest()
    print(type(hash))
    x = unpack_bigint(hash)
    # x = int.from_bytes(hash, byteorder='big')
    sksign = RSA.importKey(sk)
    # print('Sig d:', sksign.d)
    # print('Sig n:', sksign.n)

    s = square_multiply(x, sksign.d, sksign.n)
    return s


def verify_sign(public_key_loc, sign, data):
    pk = open(public_key_loc, 'r').read()
    pksign = RSA.importKey(pk)
    s = unpack_bigint(sign)

    xprime = square_multiply(s, pksign.e, pksign.n)

    # Get hash value of the plaintext
    x = SHA256.new(data).digest()
    x1 = unpack_bigint(x)
    # print('x:', x)
    # print('x1:', x1)
    # print('xprime:', xprime)

    if xprime == x1:
        print('Verification successful!')

    else:
        print('Error: Wrong message')

# Part 2: Protocol attack
def RSA_attack_enc(public_key_file, message):
    pk = open(public_key_file, 'r').read()
    pkrsa = RSA.importKey(pk)
    m = square_multiply(message, pkrsa.e, pkrsa.n)
    return m

def RSA_attack_dec(private_key_file, cipher):
    sk = open(private_key_file, 'r').read()
    skrsa = RSA.importKey(sk)
    m = square_multiply(cipher, skrsa.d, skrsa.n)
    return m

# Part 3: Implementing RSA with Padding
def encrypt_pad_RSA(public_key_file, message):
    pk = open(public_key_file, 'r').read()
    pkrsa = RSA.importKey(pk)
    print('pk pad key length:', len(pk))
    key = PKCS1_OAEP.new(pkrsa)
    m = key.encrypt(message)
    return m

def decrypt_pad_RSA(private_key_file, cipher):
    sk = open(private_key_file, 'r').read()
    skrsa = RSA.importKey(sk)
    print('sk pad key length:', len(sk))
    key = PKCS1_OAEP.new(skrsa)
    m = key.decrypt(cipher)
    return m

def sign_pad_RSA(private_key_loc, data):
    sk = open(private_key_loc, 'r').read()
    sksign = RSA.importKey(sk)
    key = PKCS1_PSS.new(sksign)
    digest = SHA256.new()
    digest.update(b64encode(data))
    signmsg = key.sign(digest)
    return signmsg

def verify_sign_pad(public_key_loc, sign, data):
    pk = open(public_key_loc, 'r').read()
    pksign = RSA.importKey(pk)
    key = PKCS1_PSS.new(pksign)
    digest = SHA256.new()
    digest.update(b64encode(data))
    if key.verify(digest, sign):
        return True
    return False



if __name__ == "__main__":
    message = open('message.txt', 'r').read().encode()
    # Encrypt RSA
    cipher = encrypt_RSA('mykey.pem.pub', message)
    print('CT:', cipher)
    cipher = pack_bigint(cipher)
    enc = b64encode(cipher)
    print('Cipher:', cipher)
    print('Result:', enc)

    # Decrypt RSA
    dec = decrypt_RSA('mykey.pem.priv', cipher)
    plaintext = pack_bigint(dec)
    print('Result:', plaintext)

    # Signature
    ciphersign = sign_RSA('mykey.pem.priv', message)
    ciphersign = pack_bigint(ciphersign)
    msgsign = b64encode(ciphersign)
    print('Signed msg:', msgsign)

    # Verification
    verify = verify_sign('mykey.pem.pub', ciphersign, message)

    # Part 2 Protocol attack
    y = 100
    s = 2
    enc_y = RSA_attack_enc('mykey.pem.pub', y)
    enc_s = RSA_attack_enc('mykey.pem.pub', s)
    ys = enc_y * enc_s
    dec_ys = RSA_attack_dec('mykey.pem.priv', ys)
    print('\nEncrypted: %s\n' % y)
    print('Result: \n%s\n' % b64encode(pack_bigint(enc_y)))
    print('Modified to: \n%s\n' % b64encode(pack_bigint(ys)))
    print('Decrypted:', dec_ys)


    # Part 3 Implementing RSA with padding
    # Encrypt
    cipher = encrypt_pad_RSA('mykey.pem.pub', message)
    print('Encrypted w pad:', b64encode(cipher))

    # Decrypt
    plaintext = decrypt_pad_RSA('mykey.pem.priv', cipher)
    print('Decrypted w pad:',plaintext)

    # Signature
    ciphersign = sign_pad_RSA('mykey.pem.priv', message)
    signmsg = b64encode(ciphersign)
    print('Signed msg w pad:', signmsg)

    # Verification
    verifypad = verify_sign_pad('mykey.pem.pub', ciphersign, message)
    print('Verify w pad:', verifypad)

    # Generating own private and public key
    priv_key, pub_key = generate_RSA(bits=1024)
    # print('My public key:', pub_key)
    # print('My private key:', priv_key)
    print('my pk key length:', len(pub_key))
    print('my sk key length:', len(priv_key))

    # Friend exchange message - To Bertha
    # Encrypting using Bertha public key
    rawsum = open('sumtobertraw.txt', 'r').read().encode()
    enctobert = encrypt_pad_RSA('bertkey.pem.pub', message)
    print('Enc msg for Bertha:', b64encode(enctobert))

    # Decrypting Bertha message with my private key
    opensum = open('encryptedfriendtesting.txt', 'r').read().encode()
    plainsum = decrypt_pad_RSA('sumkey.pem.priv', opensum)
    print('Open Bertha msg to me:', plainsum)


    # mydata part
    # Signing with my private key
    mydata = open('mydata.txt', 'r').read().encode()
    signdata = sign_pad_RSA('sumkey.pem.priv', mydata)
    print('Signed data:', b64encode(signdata))
    # signed data is under 'mydatasumsign', Bertha will open it using my public key

