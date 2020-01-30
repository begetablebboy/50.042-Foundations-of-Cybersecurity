"""
    Part 3 - Break Hash: Brute Forcing
    Sumedha 1002876

"""

import hashlib
import itertools
from time import time
import random

# iterate through the string of alphabets and numbers
# then store the hash value as a key, the actual word is the value in the dictionary
# compare the hash value with the hash string that was given

alphabetsnum = "abcdefghijklmnopqrstuvwxyz0123456789"
salt = "abcdefghijklmnopqrstuvwxyz"
password_dict = {}
crackedpwd = []
givenhash = []
salt_dict ={}

file = open('hash5.txt', 'r')
# print(file.readlines())

for element in [line.rstrip().split() for line in open('hash5.txt','r')]:
    # print(md5hash)
    for hash in element:
        givenhash.append(hash)

# print(givenhash)


# md5hash = input("Provide the hashed password: ")

counter = 0
for pwd in itertools.product(alphabetsnum, repeat=5):
    strpwd = ''.join(pwd)
    hashpwd = hashlib.md5(strpwd.encode('utf-8')).hexdigest()
    password_dict[strpwd] = hashpwd
    # print(password_dict)

    start = time()
    for md5hash in givenhash:
        if md5hash == hashpwd:
            crackedpwd.append(strpwd)
            end = time()
            duration = end - start
            counter += 1
            print("Password", counter, "is: ", strpwd)
            print("Time taken to crack password", counter, ": ", start, "-", end, "=", duration)


file.close()