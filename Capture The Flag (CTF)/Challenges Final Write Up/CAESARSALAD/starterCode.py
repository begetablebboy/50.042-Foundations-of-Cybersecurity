from Crypto.PublicKey import RSA
from base64 import b64decode, b64encode
import math


def square_multiply(a, x, n):  # a^x (mod n)
    y = 1
    binStringX = bin(x)[2:]
    for i in binStringX:
        y = (y * y) % n
        if i == '1':
            y = (y * a) % n
    return y


# function to convert long int to byte string
def pack_bigint(i):
    b = bytearray()
    while i:
        b.append(i & 0xFF)
        i >>= 8
    return b


# function to convert byte string to long int
def unpack_bigint(b):
    b = bytearray(b)
    return sum((1 << (bi * 8)) * bb for (bi, bb) in enumerate(b))

def mod_inverse(x, y):
    # See: http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    def eea(a, b):
        if b == 0: return (1, 0)
        (q, r) = (a // b, a % b)
        (s, t) = eea(b, r)
        return (t, s - (q * t))

    inv = eea(x, y)[0]
    if inv < 1:
        inv += y  # we only want positive values
    print('t:', inv)
    return inv


# ϕ(n) = (p-1)*(q-1)
def totient_n(p, q):
    totient = (p-1)*(q-1)
    return totient

if __name__ == "__main__":
    # Extended Euclidean Algorithm to find Private key
    # For pubKey1 and ct1
    p1 = 293049347
    q1 = 447620901583917369406703727865417431168683
    n1 = 131175012912718250806592304873426282086400000000001
    e1 = 11
    totient_n1 = totient_n(p1, q1)
    print('Finding private key 1 (t): ')
    key1 = mod_inverse(e1, totient_n1)

    # Decrypting ct2 with pubKey1
    cipher1 = open('ct2.txt', 'r').read().encode()
    # print(cipher1)
    b64cipher1 = b64decode(cipher1)
    # print(b64cipher1)
    ct1 = unpack_bigint(b64cipher1)
    print('ct1:', ct1)

    # Decipher ct1 after finding private key 1
    dec_ct1 = square_multiply(ct1, key1, n1)
    pack_dec_ct1 = pack_bigint(dec_ct1)
    print('dec_ct1:', pack_dec_ct1)


    # Extended Euclidean Algorithm to find Private key
    # For pubKey2 and ct2
    p2 = 52750358975649354449407
    q2 = 23574637757246841069594107658796543
    n2 = 1243570604415668070026688632353250776486772736000000000001
    e2 = 23
    totient_n2 = totient_n(p2, q2)
    print('\nFinding private key 2 (t): ')
    privatekey2 = mod_inverse(e2, totient_n2)

    # Decrypting ct1 with pubKey2
    cipher2 = open('ct1.txt', 'r').read().encode()
    b64cipher2 = b64decode(cipher2)
    ct2 = unpack_bigint(b64cipher2)
    print('ct2:', ct2)

    # Decipher ct1 after finding private key 1
    dec_ct2 = square_multiply(ct2, privatekey2, n2)
    pack_dec_ct2 = pack_bigint(dec_ct2)
    print('dec_ct2:', pack_dec_ct2)

    # Using an online decoder: https://www.dcode.fr/ascii-shift-cipher
    # ct1: 	iib_2100h}, shift by 115/13
    # ct2: CTF{SUTD_l , shift by 114
    # Combine both ct1 and ct2 = CTF{SUTD_lib_2100h}