#50.042 FCS Lab 6 template
#Year 2019

import math
import primes_template

# size of square root for the group order
def grpsize(p):
    size = int(math.floor(math.sqrt(p-1)))
    return size

def baby_step(alpha,beta,p,fname):
    m = grpsize(p)
    fid = open(fname, 'w')
    for baby in range(m):
        exponentation = (primes_template.square_multiply(alpha,baby,p)*beta) % p
        fid.write(str(exponentation) + ',' + str(baby) + '\n')
    fid.close()
    
def giant_step(alpha,p,fname):
    m = grpsize(p)
    fid = open(fname, 'w')
    for giant in range(m):
        exponentation = primes_template.square_multiply(alpha, m*giant, p)
        fid.write(str(exponentation) + ',' + str(giant) + '\n')
    fid.close()

def baby_giant(alpha,beta,p):
    m = grpsize(p)
    baby_step(alpha,beta,p,'right.txt')
    giant_step(alpha,p,'left.txt')
    fleft = open('left.txt', 'r')
    fright = open('right.txt', 'r')
    rdict = {}
    for line in fright:
        # print(line)
        right, baby = line.split(',')
        rdict[int(right)] = int(baby)
    ldict = {}
    for line in fleft:
        left, giant = line.split(',')
        ldict[int(left)] = int(giant)
    fright.close()
    fleft.close()

    for right in rdict.keys():
        if right in ldict.keys():
            output = (ldict[right]*m-rdict[right]) % p
            return output

"""
# of bits the key needs to avoid attack = 30 bits
"""

if __name__=="__main__":
    """
    test 1
    My private key is:  264
    Test other private key is:  7265
    
    """
    p = 17851
    alpha = 17511
    A = 2945
    B = 11844
    sharedkey = 1671
    a = baby_giant(alpha,A,p)
    b = baby_giant(alpha,B,p)
    guesskey1 = primes_template.square_multiply(A,b,p)
    guesskey2 = primes_template.square_multiply(B,a,p)
    print('Guess key 1:', guesskey1)
    print('Guess key 2:', guesskey2)
    print('Actual shared key :', sharedkey)

