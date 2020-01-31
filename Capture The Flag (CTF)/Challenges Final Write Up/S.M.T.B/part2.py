''' For Part 2: RSA '''

# there are 11 blocks in total
# aka 22 characters per block
def split11(s):
    blist = [s[i:i+22] for i in range(0, len(s), 22)]
    print(blist)
    # Convert byte to hex
    # hlist = []
    # for i in blist:
    #     h = hex(int(i, 2))
    #     hlist.append(h)
    # print(hlist)
    return blist


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


# ϕ(n) = (p-1)*(q-1)
def totient_n(p, q):
    totient = (p-1)*(q-1)
    return totient


# Private key
def mod_inverse(x, y):
    def eea(a, b):
        if b == 0: return (1, 0)
        (q, r) = (a // b, a % b)
        (s, t) = eea(b, r)
        return (t, s - (q * t))

    inv = eea(x, y)[0]
    if inv < 1:
        inv += y  # we only want positive values
    print('private key, t:', inv)
    return inv

def bintoint(l):
    ict = []
    for i in l:
        int_i = int(i, 2)
        ict.append(int_i)
    print(ict)
    return ict


def sqmult_per_blk(lst, private, n):
    dec_list = []
    for i in lst:
        dec = square_multiply(i, private, n)
        dec_list.append(dec)
    print(dec_list)
    return dec_list


def hextoascii(txt):
    lst = []
    for i in txt:
        pack = pack_bigint(i)
        # conv = bytes.fromhex(pack)
        lst.append(pack)
    print(lst)
    return lst



if __name__ == "__main__":
    ct = open('ciphertext.txt', 'r').read().encode()
    # ct_pack = unpack_bigint(ct)
    # print(ct_pack)
    # length of ct = 242
    # print(len(ct))
    blist = split11(ct)
    # print('list:', blist[1])
    intlist = bintoint(blist)
    p = 1597
    q = 1789
    e = 1531081
    n = 2857033
    totient = totient_n(p,q)
    print('totient:', totient)
    private = mod_inverse(e, totient)
    plaintext = sqmult_per_blk(intlist, private, n)
    final = hextoascii(plaintext)
    print()