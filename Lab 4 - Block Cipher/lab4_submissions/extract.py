#!/usr/bin/env python3
# ECB plaintext extraction skeleton file for 50.042 FCS

"""
    Sumedha 1002876
"""

# python3 extract.py -i letter.e -o openletter -hh header.pbm
# openletter is in bpm format so need to convert to ppm (Used online converter)
# once converted to ppm, then convert to png (Used online converter)

import argparse

def getInfo(headerfile):
    pass

def extract(infile,outfile,headerfile):
    fin = open(infile, 'rb')
    fout = open(outfile, 'wb')
    head = open(headerfile, 'rb')

    # read the first 8 bit first
    filein = fin.read(8)
    header = head.read(8)
    # output: b'P1\n#img\n'
    # print(filein)
    # output: b'\xe9Q~\xf7\xaaY\xa5\xf4'
    # print(head.read())
    # output: b'P1\n#img\n640 480'
    # print(filein.read())
    # output: \xa1\x0b\xff\x92\xfdAyz (most repetitive)

    bytestring = b''
    # as long as the next 8 bits are still within the bit length of header
    while header:
        bytestring += header
        filein = fin.read(8)
        header = head.read(8)

    # start on a new line to separate the header from the actual image content (similar format to Tux.ppm)
    bytestring += b"\n"

    while filein:
        if filein == b'z\xa1\x0b\xff\x92\xfdAy':
            bytestring += b'11111111'
        else:
            bytestring += b'00000000'
        filein = fin.read(8)

    fout.write(bytestring)
    fin.close()
    head.close()
    fout.close()





if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Extract PBM pattern.')
    parser.add_argument('-i', dest='infile',help='input file, PBM encrypted format')
    parser.add_argument('-o', dest='outfile',help='output PBM file')
    parser.add_argument('-hh', dest='headerfile',help='known header file')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    headerfile=args.headerfile

    print('Reading from: %s'%infile)
    print('Reading header file from: %s'%headerfile)
    print('Writing to: %s'%outfile)

    success=extract(infile,outfile,headerfile)


