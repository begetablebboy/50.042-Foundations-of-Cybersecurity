#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# Simple file read in/out

#Part 3:
# The Key=246 is needed to decrypt the flag file. It is a Switzerland flag (red background, white cross).

# Import libraries
import sys
import argparse, string

def doStuff(filein, fileout, key, mode):
    # open file handles to both files
    fin = open(filein, mode='r', encoding='utf-8', newline='\n')  # read mode
    fin_b = open(filein, mode='rb')  # binary read mode
    fout = open(fileout, mode='w', encoding='utf-8', newline='\n')  # write mode
    fout_b = open(fileout, mode='wb')  # binary write mode
    #c = fin.read()  # read in file into c as a str
    # and write to fileout

    # close all file streams
    fin.close()
    fin_b.close()
    fout.close()
    fout_b.close()

    # PROTIP: pythonic way
    if mode == "e":
        with open(filein, mode="r", encoding='utf-8', newline='\n') as fin:
            plaintext = fin.read()
            bytetext = bytearray(plaintext, 'utf-8')
            ciphertext = bytearray()
            print(bytetext)

            with open(fileout, mode="wb+") as fout:
                print("byte text: ", ciphertext)
                fout.write(ciphertext)

            if 0 <= int(key) < 256:

                # convert text to binary

                for i in range (len(plaintext)):
                    #print("key: ", key)
                    # print("bytetext: ", bytetext[i])
                    # print(type(bytetext[i]))
                    # print(type(key))
                    ciphertext.append((bytetext[i] + int(key)) % 256)


                with open(fileout, mode="wb+") as fout:
                    # print('WRITING OUT\n')
                    # print("encrypted text: ", ciphertext)
                    fout.write(ciphertext)


            else:
                print("key out of range")



    elif mode == "d":
        with open(filein, mode="rb") as fin:
            entext = fin.read()
            bytetext = bytearray(entext)
            deciphertext = bytearray()


            if 0 <= int(key) < 256:
                for i in bytetext:
                    # Formula = (byte - key) % 256)
                    deciphertext.append((i - int(key)) % 256)

                with open(fileout, mode="wb+") as fout:
                    #print(deciphertext)
                    fout.write(deciphertext)

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