import sys
import argparse

lowerKeyBoundary = 0
upperKeyBoundary = 255


def encrypt(ba, key):
    baEncrypt = bytearray(map(lambda x: (x+int(key))%256, ba))
    return baEncrypt

def decrypt(baEncrypt, key):
    baDecrypt = bytearray(map(lambda x: (x-key+256)%256, baEncrypt))
    return baDecrypt


def shiftCipher(filein,fileout, key, mode):
    # Validate the mode
    valid_modes = ['d', 'e', 'D', 'E']
    if mode not in valid_modes:
        raise Exception('Please enter a valid mode, you can choose d, e, D or E')
    key = int(key)
    # Validate the key that it is an integer # isinstance(<var>, int)
    # if isinstance(key, int) or key.isdigit(): #str.isdigit():
    #     if key < lowerKeyBoundary or key > upperKeyBoundary:
    #         raise Exception('The key length should be between 0 and 255')
    # else:
    #     raise Exception('Key should be an integer')
    with open(filein, 'br') as file:
        ba = bytearray(file.read())
        switcher = {
                'd': decrypt,
                'D': decrypt,
                'e': encrypt,
                'E': encrypt
            }
        # Check the string format
        func = switcher.get(mode, lambda: "Invalid mode")
        baNew = func(ba, key)  
    
    with open(fileout, 'bw') as file:
        file.write(baNew)

# our main function
if __name__=="__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein',help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')
    parser.add_argument('-k', dest='key',help='key')
    parser.add_argument('-m', dest='mode', help='mode')

    # parse our arguments
    args = parser.parse_args()
    filein=args.filein
    fileout=args.fileout
    key = args.key
    mode = args.mode

    shiftCipher(filein,fileout, key, mode)