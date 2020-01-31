def decrypt(message):
    msgint = [ord(i) for i in message]
    key = '20191202'
    dict = []
    dict2 = []
    dict3 = []
    dict4 = []
    dict5 = []
    dict6 = []
    dict7 = []
    dict8 = []
    dict9 = []
    H1 = '012'
    H2 = '0123456789'
    M1 = '012345'
    M2 = '0123456789'
    pt = ''
    final = ''
    # Understanding that from C code, numbers, punctuation and spaces doesn't get shifted.
    for i in range(2):
        v = int(msgint[i]) - int(key[i])
        pt += chr(v)
    #print(pt)
    pt += chr(int(msgint[2]))
    pt += chr(int(msgint[3]))
    pt += chr(int(msgint[4]))
    #print(pt)
    for i in range(5,6):
        v = int(msgint[i]) - int(key[i])
        pt += chr(v)
    #print(pt)
    pt += chr(int(msgint[6]))
    pt += chr(int(msgint[7]))
    print(pt)
    # Until here, we are able to deduce part of the key based on the scheme we see from the C code which is YYYYMMDD
    # In order to continue to find out the hhmmss:

    for i in range(8, 9):
        for k in range(len(H1)):
            text = ''
            v = int(msgint[i]) - int(H1[k])
            text += pt
            text += chr(v)
            dict.append(text)
    print(dict)
    # Since all 3 are possible, we continue with the inputs of all 3. And since we know that numbers don't change we just simply add the next one which is 0 into each ele of dict.
    for i in range(len(dict)):
        text = ''
        text += str(dict[i])
        text += chr(int(msgint[9]))
        dict2.append(text)
    print(dict2)
    # Since it looks like it can form an english word like the first part which spells engine, we can see that only
    # g0 and f0 can follow an english word, thus we ignore dict2[2].
    for i in range(10,11):
        for k in range(len(M1)):
            for l in range(0,2):
                text = ''
                v = int(msgint[i]) - int(M1[k])
                text += str(dict2[l])
                text += chr(v)
                dict3.append(text)
    print(dict3)
    # Knowing that only dict3[0], dict3[1], dict3[6], dict3[7], dict3[8] and dict3[9] can follow an english word
    newtest = []
    newtest.append(0)
    newtest.append(1)
    newtest.append(6)
    newtest.append(7)
    newtest.append(8)
    newtest.append(9)
    # print(len(newtest))
    # Here is a bit tricky because in C shifting a will result in going back to z instead of the usual ascii ', thus we have to manually shift here.
    for i in newtest:
        test = ''
        test += str(dict3[i])
        test += chr(int(msgint[11]))
        dict4.append(test)
    #print(dict4)
    for i in range(0,9):
        for k in newtest:
            # 122 is the # for z which is if u shfit a by 1 backwards.
            text = ''
            v = 122 - i
            text += str(dict3[k])
            text += chr(v)
            dict4.append(text)
    print(dict4)
    # Next is a number so there's no change, therefore we just add it to the elements in dict4.
    for i in range(len(dict4)):
        text = ''
        v = int(msgint[12])
        text += str(dict4[i])
        text += chr(v)
        dict5.append(text)
    print(dict5)
    # Here we notice that dict5[26] is the only one that follows an english word.
    for i in range(13,14):
        for k in range(len(M2)):
            text = ''
            v = int(msgint[i]) - int(M2[k])
            text += str(dict5[25])
            text += chr(v)
            dict6.append(text)
    print(dict6)
    # Only dict6[2] can follow an english word

    # From the scheme that we got from the C code, we can see that tfor the last 6 elements, they are a repeat of
    # HHMMSS, so we will use the same values that are used from 8 to 13 to shift. From 8 we can see that its shifted
    # by 1, from 9 we cant tell yet as its a number, from 10 we can see that it is shited by 0, from 11 we can see
    # that its shifted by 4, from 12 we cant tell yet as its an number, for 13 we can see that its shifted by 2. So
    # we are gonna add them all together and see if we can deduce the word from there.
    final += str(dict6[2])
    final += chr(int(msgint[14]) - 1)
    print(final)
    for i in range(len(H2)):
        text = ''
        v = int(msgint[15]) - int(H2[i])
        text += final
        text += chr(v)
        dict7.append(text)
    print(dict7)
    for i in range(len(dict7)):
        text = ''
        text += str(dict7[i])
        text += chr(int(msgint[16]))
        dict8.append(text)
    print(dict8)
    for i in range(len(dict8)):
        text = ''
        text += str(dict8[i])
        text += chr(int(msgint[17]) - 4)
        dict9.append(text)
    print(dict9)
    # From here we can pretty much guess the next letter is D because ISTD, so we know that 12 is shifted by 5
    finalfinal = ''
    finalfinal += str(dict9[9])
    finalfinal += chr(int(msgint[18]) - 5)
    print(finalfinal)
    # Finally the last one is shifted by 2
    output = ''
    output += finalfinal
    output += chr(int(msgint[19]) - 2)
    print('CTF{%s}' % output)



decrypt('Gn 6!p3_g0ra0teRSXIw')
#20191202190452190452s
#En 6!n3_f0rw0rdISTDu
