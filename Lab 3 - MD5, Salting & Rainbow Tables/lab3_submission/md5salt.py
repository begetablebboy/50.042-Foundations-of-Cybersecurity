"""
    Part 5 - Salting
    Sumedha 1002876

"""

import hashlib
import random


alphabetsnum = "abcdefghijklmnopqrstuvwxyz0123456789"
salt = "abcdefghijklmnopqrstuvwxyz"
pwd_list = ['aseas', 'cance', 'di5gv', 'dsmto', 'egunb', 'hed4e', 'lou0g', 'mldhi', 'nized', 'ofror', 'opmen', 'owso9', 'sso55', 'tpoin', 'tthel']
salt_dict ={}

file = open('pass6.txt', 'a+')
sfile = open('salted6.txt', 'a+')

for pwd in pwd_list:
    pwd = pwd + random.choice(salt)
    hashsaltpwd = hashlib.md5(pwd.encode('utf-8')).hexdigest()
    salt_dict[pwd] = hashsaltpwd
    file.write(pwd + "\n")
    sfile.write(hashsaltpwd + "\n")


file.close()
sfile.close()