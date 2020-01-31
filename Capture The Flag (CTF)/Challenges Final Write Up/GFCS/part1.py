''' To access the Zip folder '''

from Crypto.PublicKey import RSA
from base64 import b64decode, b64encode


n = 91348998827750122993315803945306966072648090575002239502799599978804238369231
e = 65537
p = 302239968944794134660889979148054548249
q = 302239968944794134818677484631621172519
c = b'J04HMUs+IsiKuiTDb1zmRPPtgK7XOcp3H4kmGzZTJKo='  # this is a b64encode

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


# Deriving the private key
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
    totient = totient_n(p, q)
    key = mod_inverse(e, totient)

    # Decrypting ct2 with pubKey1
    b64c = b64decode(c)
    dec = unpack_bigint(b64c)
    print('ct1:', dec)

    # Decipher
    dec_c = square_multiply(dec, key, n)
    pack_dec_c = pack_bigint(dec_c)
    print('dec_ct1:', pack_dec_c)