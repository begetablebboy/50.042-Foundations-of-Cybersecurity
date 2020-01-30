''' For own reference/practice: Familiarizing with shift cipher '''

def encrypt(plaintext,key,mode):
    result = ""
    #print(key)
    #print(len(plaintext))

    #for key in range (0,len(plaintext)):
    if (key > 0) and key <= (len(plaintext) - 1):
        # print(key)
        # print(plaintext)
        if mode == "e":
            for i in range(len(plaintext)):
                char = plaintext[i]

                # Encrypt uppercase characters
                if char.isupper():
                    result += chr((int(ord(char)) + int(key)))

                # Encrypt lowercase characters
                else:
                    result += chr((int(ord(char)) - int(key)))

            return result

        else:
            print("decipher not implemented")


    else:
        print("key out of range")


def decrypt(encrypttext,key):
    result = " "

    if (key > 0 and key <= (len(encrypttext) - 1)):
        #print(key)
        # print(encrypttext)
        #if(mode == "d"):
            for i in range(len(encrypttext)):
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

# Check
plaintext = "ATTACKATONCE"
key = 4
mode = 'e'
print("En-Text : " + plaintext)
print("Key : " + str(key))
print("Cipher: " + encrypt(plaintext, key, mode))


encrypttext = 'EXXEGOEXSRGI'
#mode = 'd'
print("De-Text : " + encrypttext)
print("Key : " + str(key))
print("Decipher: " + decrypt(encrypttext, key))
