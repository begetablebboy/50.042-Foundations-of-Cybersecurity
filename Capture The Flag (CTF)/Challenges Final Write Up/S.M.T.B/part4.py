import pyaes
import pbkdf2
import binascii, os, secrets

''' Password to Key Derivation '''
passwordSalt = b'\x7f\x8a\x91\xab\xc2\x0c\xe6\x8d\xc0\xd7\xba!\xd2\x80\xa1M'
password = 's3cr3t*c0d3'
key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
print('AES encryption key1:', binascii.hexlify(key))


# ct1 = b'cee979b86e2c59f6caab3c6055fbfa'
# ct2 = b'c9ee7aa5693542f0d7b63a615af6'
# ct3 = b'ccf27fb3733944e0'
# ct4 = b'c9f371b069'

''' AES Decryption (CTR Block Mode) '''
ct1 = open('ct1.txt', 'r').read().encode()
ct2 = open('ct2.txt', 'r').read().encode()
ct3 = open('ct3.txt', 'r').read().encode()
ct4 = open('ct4.txt', 'r').read().encode()
unhex1 = binascii.unhexlify(ct1)
unhex2 = binascii.unhexlify(ct2)
unhex3 = binascii.unhexlify(ct3)
unhex4 = binascii.unhexlify(ct4)
# print(unhex1)
# print(unhex2)
# print(unhex3)
# print(unhex4)
iv = 57116448576878005380785937564945681393249968307171981972903895716101015138040
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
# Transpositional
# decrypted1 = aes.decrypt(unhex1)
# # print('ct1:', unhex1)
# print('Decrypted ct1:', decrypted1)

# Substitutional
# decrypted2 = aes.decrypt(unhex2)
# # print('ct2:', unhex2)
# print('Decrypted ct2:', decrypted2)

#  Vigenere
# decrypted3 = aes.decrypt(unhex3)
# # print('ct3:', unhex3)
# print('Decrypted ct3:', decrypted3)

#  Shift
decrypted4 = aes.decrypt(unhex4)
# print('ct4:', unhex4)
print('Decrypted ct4:', decrypted4)