#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.042 FCS

"""
    Sumedha 1002876
"""

from present import *
import argparse

nokeybits=80
blocksize=64



def ecb(infile,outfile,key,mode):
    fin = open(infile, 'rb')
    fout = open(outfile, 'wb')
    key = open(key, 'rb')
    ciphertext = b''

    # 64 bits = 8 bytes, read block by block
    txtfile = fin.read(8)
    key1 = key.read()

    # Encryption
    # python3 ecb.py -i Tux.ppm -o Tuxenc -k key.txt -m e
    if mode == 'e':
        # read block by block
        while txtfile != b'':
            # from_bytes convert everything to int
            plaintext = int.from_bytes(txtfile, byteorder='big')
            # to_bytes convert everything to bytes
            # present is encryption and only take int for key
            ciphertext += present(plaintext, int(key1)).to_bytes(8, byteorder='big')
            # move on to the next 8 bytes
            txtfile = fin.read(8)

    # Decryption
    # python3 ecb.py -i Tuxenc -o Tuxdec -k key.txt -m e
    if mode == 'd':
        while txtfile != b'':
            plaintext = int.from_bytes(txtfile, 'big')
            ciphertext += present_inv(plaintext, int(key1)).to_bytes(8, 'big')
            txtfile = fin.read(8)


    # use w when want to output
    fout.write(ciphertext)
    fin.close()
    fout.close()
    key.close()

# Used https://www.coolutils.com/online/PPM-to-PNG# to open the ppm file,
# since unable to use imagemagick
# Tuxenc will not be able to be converted from ppm to png
# Tuxdec will be able to be converted from ppm to png (To check)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode')

    args = parser.parse_args()
    infile = args.infile
    outfile = args.outfile
    keyfile = args.keyfile
    mode = args.mode

    ecb(infile,outfile,keyfile,mode)

