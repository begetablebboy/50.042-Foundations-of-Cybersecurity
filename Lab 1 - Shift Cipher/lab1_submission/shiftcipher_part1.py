#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# Simple file read in/out


# Import libraries
import sys
import argparse, string

def doStuff(filein, fileout, key, mode):
    # open file handles to both files
    fin = open(filein, mode='r', encoding='utf-8', newline='\n')  # read mode
    fin_b = open(filein, mode='rb')  # binary read mode
    fout = open(fileout, mode='w', encoding='utf-8', newline='\n')  # write mode
    fout_b = open(fileout, mode='wb')  # binary write mode
    c = fin.read()  # read in file into c as a str
    # and write to fileout

    # close all file streams
    fin.close()
    fin_b.close()
    fout.close()
    fout_b.close()

    # PROTIP: pythonic way
    with open(filein, mode="r", encoding='utf-8', newline='\n') as fin:
        text = fin.read()
        # do stuff

        if mode == "e":
            output = encrypt(text, key)

        elif mode == "d":
            output = decrypt(text, key)
        # file will be closed automatically when interpreter reaches end of the block

        with open(fileout, mode="w", encoding='utf-8', newline='\n') as fout:
            fout.write(output)

def encrypt(plaintext, key):
    result = ""
    # print(key)
    # print(len(plaintext))

    if (int(key) > 0) and int(key) <= (len(string.printable) - 1):
        # print(key)
        # print(plaintext)
        for i in range(len(plaintext)):
            #print(len(plaintext))
            char = plaintext[i]

            # Encrypt uppercase characters
            if char.isupper():
                result += chr((int(ord(char)) + int(key)))

            # Encrypt lowercase characters
            else:
                result += chr((int(ord(char)) + int(key)))

        return result

    else:
        print("key out of range")


def decrypt(encrypttext, key):
    result = ""

    if (int(key) > 0) and int(key) <= (len(string.printable) - 1):
        # print(key)
        # print(encrypttext)
        # if(mode == "d"):
        for i in range(len(encrypttext)):
            #print(len(encrypttext))
            char = encrypttext[i]

            # Decrypt upper characters
            if char.isupper():
                result += chr((int(ord(char)) - int(key)))

            # Decrypt lower characters
            else:
                result += chr((int(ord(char)) - int(key)))

        return result


    else:
        print("key out of range")


# our main function
if __name__=="__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein',help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')
    parser.add_argument('-k', dest='key', help='key')
    parser.add_argument('-m', dest='mode', help='mode')

    # parse our arguments
    args = parser.parse_args()
    filein=args.filein
    fileout=args.fileout
    key = args.key
    mode = args.mode

    doStuff(filein, fileout, key, mode)

    # all done
