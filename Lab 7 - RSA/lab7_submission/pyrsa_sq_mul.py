from Crypto.PublicKey import RSA
from base64 import b64encode,b64decode
import random

def square_multiply(a,x,n):
    result = 1
    x_bin = bin(x)[2:]
    for i in x_bin:
        result = result * result % n
        if i == '1':
            result = result * a % n
    return result

# function to convert long int to byte string
def pack_bigint(i):
    b=bytearray()
    while i:
        b.append(i&0xFF)
        i>>=8
    return b

# function to convert byte string to long int
def unpack_bigint(b):
    b=bytearray(b)
    return sum((1<<(bi*8))* bb for (bi,bb) in enumerate(b))

if __name__=="__main__":
    pass
