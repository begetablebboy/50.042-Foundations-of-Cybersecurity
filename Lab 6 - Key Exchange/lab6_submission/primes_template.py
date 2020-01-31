#50.042 FCS Lab 6 template
# Year 2019

import random

def square_multiply(a,x,n):
    result = 1
    # convert x (int) into binary
    # [2:] removes '0b'
    x_bin = bin(x)[2:]
    for i in x_bin:
        result = result*result % n
        # multiply only if the bit of x_bin at i is 1
        if i == '1':
            result = result*a % n
    return result

# an algorithm that determines whether a given number is prime
def miller_rabin(n, a):
    # ^ - power not XOR in comments, on execution is **
    # if it is an even number, it is a composite number
    # Step 1: Find n-1 = 2^k*m (GOAL)
    if n == 2 or n == 3:
        return True

    if n%2 == 0:
        return False

    r = 0
    q = n-1
    while q % 2 == 0:
        r += 1
        # // rounds the result down to the nearest whole number
        q = q//2

    for i in range(a):
        # Step 2: select an 'k' from 1 < k < n-1
        # random.randrange used to generate random number
        k = random.randrange(2, n-1)

        # Step 3: Compute bo = a^m mod n, bi = bi-1^2
        # pow(x,y,a) = x^y mod a
        isprime = pow(k,q,n)
        if isprime == 1 or isprime == n-1:
            continue
        for i in range(r-1):
            isprime = pow(isprime,2,n)
            if isprime == n-1:
                break
        else:
            return False
    return True

def isitprime(input):
    if input < 2:
        return False
    a =2
    return miller_rabin(input,a)

def gen_prime_nbits(n):
    while True:
        input = random.randrange(2**(n-1),2**n)
        if isitprime(input):
            return input


if __name__=="__main__":
    print('Is 561 a prime?')
    print(miller_rabin(561,2))
    print('Is 27 a prime?')
    print(miller_rabin(27,2))
    print('Is 61 a prime?')
    print(miller_rabin(61,2))

    print('Random number (100 bits):')
    print(gen_prime_nbits(100))
    print('Random number (80 bits):')
    print(gen_prime_nbits(80))
