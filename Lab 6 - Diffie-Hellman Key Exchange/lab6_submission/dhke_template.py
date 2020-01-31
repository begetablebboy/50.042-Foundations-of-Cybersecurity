#50.042 FCS Lab 6 template
#Year 2019

"""
What are the advantages and disadvantages of DHKE?
Advantages:
1. DHKE allows 2 parties with no prior knowledge of each other to jointly establish a
shared secret key over an insecure channel.
2. Sharing of secret key is safe.

Disadvantages:
1. DHKE cannot be used for asymmetric key exchange.
2. DHKE cannot be used for signing digital signatures.
3. DHKE is prone to man-in-the-middle attack since it does not authenticate either
party involved in the exchange.
"""

import primes_template
import random
import sys


def dhke_setup(nb):
    # prime number closest to 2^80 = 1208925819614629174706189
    p = 1208925819614629174706189
    alpha = random.randint(2,p-2)
    return p, alpha

def gen_priv_key(p):
    sk = random.randint(1,sys.maxsize)
    # print(sk)
    return sk

def get_pub_key(alpha, a, p):
    pk = primes_template.square_multiply(alpha,a,p)
    return pk

def get_shared_key(keypub,keypriv,p):
    shared = primes_template.square_multiply(keypub, keypriv, p)
    return shared
    
if __name__=="__main__":
    p,alpha= dhke_setup(80)
    print('Generate P and alpha:')
    print('P:',p)
    print('alpha:', alpha)
    print
    a=gen_priv_key(p)
    b=gen_priv_key(p)
    print('My private key is: ',a)
    print('Test other private key is: ',b)
    print
    A=get_pub_key(alpha,a,p)
    B=get_pub_key(alpha,b,p)
    print('My public key is: ',A)
    print('Test other public key is: ',B)
    print
    sharedKeyA=get_shared_key(B,a,p)
    sharedKeyB=get_shared_key(A,b,p)
    print('My shared key is: ',sharedKeyA)
    print('Test other shared key is: ',sharedKeyB)
    print('Length of key is %d bits.'%sharedKeyA.bit_length())



