#!/usr/bin/python3
# -*- coding: utf-8 -*-
# DA+Nils 2018
# Andrei + Z.TANG + Bowen, 2019

"""
Lab2: Breaking Ciphers

Pwntool client for python3

Install: see install.sh

Documentation: https://python3-pwntools.readthedocs.io/en/latest/

Sol1: The plaintext is the story of the Little Red Cap
"""

""" Sumedha 1002876 """

import PyPDF2
import operator
from pwn import remote
from collections import Counter


# pass two bytestrings to this function
def XOR(a, b):
    r = b''
    for x, y in zip(a, b):
        r += (x ^ y).to_bytes(1, 'big')
    return r


def sol1():
    # arrange the table in descending frequency order
    # then map it to the standard frequency table (100)
    # sequenceMatcher(none,sth ,sth)

    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("1")  # select challenge 1

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    # decrypt the challenge here
    challenge = challenge.decode('utf-8')
    # print(type(challenge)) # String
    # print(challenge)
    # Checking frequency of each letters in the ciphertext
    all_freq = {}
    for i in challenge:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    # print(all_freq)
    # Sort in descending order
    descending = dict(sorted(all_freq.items(), key=operator.itemgetter(1), reverse=True))
    print(descending)

    # Extracting text from PDF file
    mermaid = open('littlemermaid.pdf', 'rb')
    readmermaid = PyPDF2.PdfFileReader(mermaid)
    # print(readmermaid)
    # print(readmermaid.numPages)

    mermaidtext = ""
    for pagenum in range (readmermaid.numPages):
        pageObj = readmermaid.getPage(pagenum)
        mermaidtext += (pageObj.extractText())
        # print(pageObj.extractText())
    #print(mermaidtext)

    mermaid_count = Counter(mermaidtext)
    # print("Mermaid:\n")
    # print(mermaid_count)
    # mermaid_freq = dict(mermaid_count)
    # print(mermaid_freq)
    mermaid.close()

    # Extract text from Classic Fairy Tales from PDF file
    classic = open('classicfairytales.pdf', 'rb')
    readclassic = PyPDF2.PdfFileReader(classic)

    classictext = ""
    for pagenum in range(readclassic.numPages):
        pageObj = readclassic.getPage(pagenum)
        classictext += (pageObj.extractText())
        # print(pageObj.extractText())
    # print(mermaidtext)

    classic_count = Counter(classictext)
    # print("Classic:\n")
    # print(classic_count)
    classic.close()

    # Extract text from Grimm Fairy Tales from PDF file
    grimm = open('grimm10.pdf', 'rb')
    readgrimm = PyPDF2.PdfFileReader(grimm)

    grimmtext = ""
    for pagenum in range(readgrimm.numPages):
        pageObj = readgrimm.getPage(pagenum)
        grimmtext += (pageObj.extractText())

    grimm_count = Counter(grimmtext)
    # print("Grimm:\n")
    # print(grimm_count)
    grimm.close()

    # Merge 3 counter dictionaries together
    # print(classic_count + mermaid_count + grimm_count)

    challenge = list(challenge)
    # Replace each characters from challenge with the characters from the long texts based on the frequency analysis
    for i in range(len(challenge)):
        if challenge[i] == '2':
            challenge[i] = ' '

        elif challenge[i] == 'O':
            challenge[i] = 'e'

        elif challenge[i] == '.':
            challenge[i] = 't'

        elif challenge[i] == 'I':
            challenge[i] = 'a'

        elif challenge[i] == 'c':
            challenge[i] = 'o'

        elif challenge[i] == 't':
            challenge[i] = 'h'

        elif challenge[i] == '\x0c':
            challenge[i] = 'r'

        elif challenge[i] == 'K':
            challenge[i] = 'n'

        elif challenge[i] == '|':
            challenge[i] = 'd'

        elif challenge[i] == '>':
            challenge[i] = 'i'

        elif challenge[i] == 'E':
            challenge[i] = 's'

        elif challenge[i] == '-':
            challenge[i] = 'l'

        elif challenge[i] == ';':
            challenge[i] = 'w'

        elif challenge[i] == '\t':
            challenge[i] = '\n'

        elif challenge[i] == ' ':
            challenge[i] = 'g'

        elif challenge[i] == 'p':
            challenge[i] = ','

        elif challenge[i] == 'F':
            challenge[i] = 'u'

        elif challenge[i] == 'Y':
            challenge[i] = 'c'

        elif challenge[i] == '_':
            challenge[i] = 'm'

        elif challenge[i] == "'":
            challenge[i] = 'y'

        elif challenge[i] == 'e':
            challenge[i] = 'f'

        elif challenge[i] == 'X':
            challenge[i] = 'p'

        elif challenge[i] == 'W':
            challenge[i] = '.'

        elif challenge[i] == '<':
            challenge[i] = 'b'

        elif challenge[i] == 'V':
            challenge[i] = 'k'

        elif challenge[i] == 's':
            challenge[i] = 'v'

        elif challenge[i] == '3':
            challenge[i] = '"'

        elif challenge[i] == 'u':
            challenge[i] = '-'

        elif challenge[i] == 'v':
            challenge[i] = "'"

        elif challenge[i] == 'R':
            challenge[i] = 'j'

        elif challenge[i] == '{':
            challenge[i] = 'q'

        elif challenge[i] == 'f':
            challenge[i] = '?'

        # elif challenge[i] == '\n':
        #     challenge[i] = 'f'


    print("".join(challenge))


    # solution = int(0).to_bytes(7408, 'big')  # default solution, write your own solution
    solution = "".join(challenge)
    conn.send(solution)
    message = conn.recvline()
    message = conn.recvline()
    if b'Congratulations' in message:
        print(message)
    conn.close()


def sol2():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("2")  # select challenge 2
    # print(message)

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()  # c
    # print(challenge)
    # some all zero mask.
    # TODO: find the magic mask!
    # mask = int(0).to_bytes(len(message), 'big')

    # There's 2 ways to do it:
    # 1. Change the specific parts of the message and then XOR
    # size of message == size of mask
    # print(len(challenge))
    # change the number at the respective position
    # mask = b'0x00\n'
    # mask = mask*33
    #
    # marray=bytearray(mask)
    # print(marray)
    #
    # marray[14] = 2
    # marray[15] = 8
    # marray[16] = 7
    # marray[17] = 6
    # marray[24] = 4

    # 2. XOR the entire mask and then XOR again with the challenge
    m_prime = bytearray('Student ID 1002876 gets 4 points\n', 'utf-8')
    m = bytearray('Student ID 1000000 gets 0 points\n', 'utf-8')
    mask = XOR(m, m_prime)

    message = XOR(challenge, mask)  # send this message to the server, have to get the mask
    conn.send(message)
    message = conn.recvline()
    message = conn.recvline()
    if b'points' in message:
        print(message)
    conn.close()


if __name__ == "__main__":
    # NOTE: UPPERCASE names for constants is a (nice) Python convention
    URL = '34.239.117.115'
    PORT = 1337

    sol1()
    sol2()
