# AES DEcryption


def BinToHex(Binary):
    Binary = str(Binary)
    BinaryP1 = Binary[0]+Binary[1]+Binary[2]+Binary[3]   # separates to first 4 bits
    BinaryP1 = int(BinaryP1,2)
    BinaryP2 = Binary[4]+Binary[5]+Binary[6]+Binary[7]   # and last 4 bits
    BinaryP2 = int(BinaryP2,2)              # converts from binary to decimal
    if BinaryP1 >9:
        BinaryP1 = chr(BinaryP1+87)      # if larger than 9 converts into relevent character, uses unicode value of a =97
    else:
        BinaryP1 = str(BinaryP1)      # # if not just keeps as number
    if BinaryP2 >9:
        BinaryP2 = chr(BinaryP2+87)
    else:
        BinaryP2 = str(BinaryP2)
    Hex = BinaryP1+BinaryP2
    return(Hex)                    # adds the two parts together


def InvSubBytes(block):

    Newblock = [[],[],[],[]]
        # S-Box
     #	    00   01   02   03   04   05   06   07   08   09   0a   0b   0c   0d   0e   0f
    R00 = ["52","09","6a","d5","30","36","a5","38","bf","40","a3","9e","81","f3","d7","fb"]
    R10 = ["7c","e3","39","82","9b","2f","ff","87","34","8e","43","44","c4","de","e9","cb"]
    R20 = ["54","7b","94","32","a6","c2","23","3d","ee","4c","95","0b","42","fa","c3","4e"]
    R30 = ["08","2e","a1","66","28","d9","24","b2","76","5b","a2","49","6d","8b","d1","25"]
    R40 = ["72","f8","f6","64","86","68","98","16","d4","a4","5c","cc","5d","65","b6","92"]
    R50 = ["6c","70","48","50","fd","ed","b9","da","5e","15","46","57","a7","8d","9d","84"]
    R60 = ["90","d8","ab","00","8c","bc","d3","0a","f7","e4","58","05","b8","b3","45","06"]
    R70 = ["d0","2c","1e","8f","ca","3f","0f","02","c1","af","bd","03","01","13","8a","6b"]
    R80 = ["3a","91","11","41","4f","67","dc","ea","97","f2","cf","ce","f0","b4","e6","73"]
    R90 = ["96","ac","74","22","e7","ad","35","85","e2","f9","37","e8","1c","75","df","6e"]
    Ra0 = ["47","f1","1a","71","1d","29","c5","89","6f","b7","62","0e","aa","18","be","1b"]
    Rb0 = ["fc","56","3e","4b","c6","d2","79","20","9a","db","c0","fe","78","cd","5a","f4"]
    Rc0 = ["1f","dd","a8","33","88","07","c7","31","b1","12","10","59","27","80","ec","5f"]
    Rd0 = ["60","51","7f","a9","19","b5","4a","0d","2d","e5","7a","9f","93","c9","9c","ef"]
    Re0 = ["a0","e0","3b","4d","ae","2a","f5","b0","c8","eb","bb","3c","83","53","99","61"]
    Rf0 = ["17","2b","04","7e","ba","77","d6","26","e1","69","14","63","55","21","0c","7d"]

    SRows = [R00,R10,R20,R30,R40,R50,R60,R70,R80,R90,Ra0,Rb0,Rc0,Rd0,Re0,Rf0]     # all the rows in order

    count = (-1)
    for row in block:          # for each row in the block
        count = count + 1
        for hexval in row:         # for all the values in each row
            sboxrow = hexval[0]
            if sboxrow.isnumeric():    # if the first part of the hex is a number
                NewHexval = SRows[int(sboxrow)]         # finds the row of sed number
            else:
                if sboxrow == "a":                          # otherwise finds the row of the letter
                    NewHexval = SRows[10]
                if sboxrow == "b":
                    NewHexval = SRows[11]
                if sboxrow == "c":
                    NewHexval = SRows[12]
                if sboxrow == "d":
                    NewHexval = SRows[13]
                if sboxrow == "e":
                    NewHexval = SRows[14]
                if sboxrow == "f":
                    NewHexval = SRows[15]

            sboxcolumn = hexval[1]
            if sboxcolumn.isnumeric():               # if the second part of the hex value is a number
                NewHexval= NewHexval[int(sboxcolumn)]      # finds the value at that numbers position in the already selected row
            else:
                if sboxcolumn == "a":                           # otherwise corresponds the letter to the number
                    NewHexval= NewHexval[10]
                if sboxcolumn == "b":
                    NewHexval= NewHexval[11]
                if sboxcolumn == "c":
                    NewHexval= NewHexval[12]
                if sboxcolumn == "d":
                    NewHexval= NewHexval[13]
                if sboxcolumn == "e":
                    NewHexval= NewHexval[14]
                if sboxcolumn == "f":
                    NewHexval= NewHexval[15]
            (Newblock[count]).append(NewHexval)         # adds the new value into a the count's (row number's) list
    return(Newblock)

def InvShiftRows(block):
    NewState = [[],[],[],[]]
    for values in block[0]:
        NewState[0].append(values)
    NewState[1].append(block[1][3])
    for i in range(0,3):
        NewState[1].append(block[1][i])
    for i in range(2,4):
        NewState[2].append((block[2])[i])
    for i in range(0,2):
        NewState[2].append((block[2])[i])
    for i in range(1,4):
        NewState[3].append(block[3][i])
    NewState[3].append(block[3][0])
    return(NewState)


def InvMixColumns(block):

    nine00 =   ["00","09","12","1b","24","2d","36","3f","48","41","5a","53","6c","65","7e","77"]
    nine01 =   ["90","99","82","8b","b4","bd","a6","af","d8","d1","ca","c3","fc","f5","ee","e7"]
    nine02 =   ["3b","32","29","20","1f","16","0d","04","73","7a","61","68","57","5e","45","4c"]
    nine03 =   ["ab","a2","b9","b0","8f","86","9d","94","e3","ea","f1","f8","c7","ce","d5","dc"]
    nine04 =   ["76","7f","64","6d","52","5b","40","49","3e","37","2c","25","1a","13","08","01"]
    nine05 =   ["e6","ef","f4","fd","c2","cb","d0","d9","ae","a7","bc","b5","8a","83","98","91"]
    nine06 =   ["4d","44","5f","56","69","60","7b","72","05","0c","17","1e","21","28","33","3a"]
    nine07 =   ["dd","d4","cf","c6","f9","f0","eb","e2","95","9c","87","8e","b1","b8","a3","aa"]
    nine08 =   ["ec","e5","fe","f7","c8","c1","da","d3","a4","ad","b6","bf","80","89","92","9b"]
    nine09 =   ["7c","75","6e","67","58","51","4a","43","34","3d","26","2f","10","19","02","0b"]
    nine0a =   ["d7","de","c5","cc","f3","fa","e1","e8","9f","96","8d","84","bb","b2","a9","a0"]
    nine0b =   ["47","4e","55","5c","63","6a","71","78","0f","06","1d","14","2b","22","39","30"]
    nine0c =   ["9a","93","88","81","be","b7","ac","a5","d2","db","c0","c9","f6","ff","e4","ed"]
    nine0d =   ["0a","03","18","11","2e","27","3c","35","42","4b","50","59","66","6f","74","7d"]
    nine0e =   ["a1","a8","b3","ba","85","8c","97","9e","e9","e0","fb","f2","cd","c4","df","d6"]
    nine0f =   ["31","38","23","2a","15","1c","07","0e","79","70","6b","62","5d","54","4f","46"]
    NineColumns = [nine00,nine01,nine02,nine03,nine04,nine05,nine06,nine07,nine08,nine09,nine0a,nine0b,nine0c,nine0d,nine0e,nine0f]
    eleven00 = ["00","0b","16","1d","2c","27","3a","31","58","53","4e","45","74","7f","62","69"]
    eleven01 = ["b0","bb","a6","ad","9c","97","8a","81","e8","e3","fe","f5","c4","cf","d2","d9"]
    eleven02 = ["7b","70","6d","66","57","5c","41","4a","23","28","35","3e","0f","04","19","12"]
    eleven03 = ["cb","c0","dd","d6","e7","ec","f1","fa","93","98","85","8e","bf","b4","a9","a2"]
    eleven04 = ["f6","fd","e0","eb","da","d1","cc","c7","ae","a5","b8","b3","82","89","94","9f"]
    eleven05 = ["46","4d","50","5b","6a","61","7c","77","1e","15","08","03","32","39","24","2f"]
    eleven06 = ["8d","86","9b","90","a1","aa","b7","bc","d5","de","c3","c8","f9","f2","ef","e4"]
    eleven07 = ["3d","36","2b","20","11","1a","07","0c","65","6e","73","78","49","42","5f","54"]
    eleven08 = ["f7","fc","e1","ea","db","d0","cd","c6","af","a4","b9","b2","83","88","95","9e"]
    eleven09 = ["47","4c","51","5a","6b","60","7d","76","1f","14","09","02","33","38","25","2e"]
    eleven0a = ["8c","87","9a","91","a0","ab","b6","bd","d4","df","c2","c9","f8","f3","ee","e5"]
    eleven0b = ["3c","37","2a","21","10","1b","06","0d","64","6f","72","79","48","43","5e","55"]
    eleven0c = ["01","0a","17","1c","2d","26","3b","30","59","52","4f","44","75","7e","63","68"]
    eleven0d = ["b1","ba","a7","ac","9d","96","8b","80","e9","e2","ff","f4","c5","ce","d3","d8"]
    eleven0e = ["7a","71","6c","67","56","5d","40","4b","22","29","34","3f","0e","05","18","13"]
    eleven0f = ["ca","c1","dc","d7","e6","ed","f0","fb","92","99","84","8f","be","b5","a8","a3"]
    ElevenColumns = [eleven00,eleven01,eleven02,eleven03,eleven04,eleven05,eleven06,eleven07,eleven08,eleven09,eleven0a,eleven0b,eleven0c,eleven0d,eleven0e,eleven0f]
    thirteen00 = ["00","0d","1a","17","34","39","2e","23","68","65","72","7f","5c","51","46","4b"]
    thirteen01 = ["d0","dd","ca","c7","e4","e9","fe","f3","b8","b5","a2","af","8c","81","96","9b"]
    thirteen02 = ["bb","b6","a1","ac","8f","82","95","98","d3","de","c9","c4","e7","ea","fd","f0"]
    thirteen03 = ["6b","66","71","7c","5f","52","45","48","03","0e","19","14","37","3a","2d","20"]
    thirteen04 = ["6d","60","77","7a","59","54","43","4e","05","08","1f","12","31","3c","2b","26"]
    thirteen05 = ["bd","b0","a7","aa","89","84","93","9e","d5","d8","cf","c2","e1","ec","fb","f6"]
    thirteen06 = ["d6","db","cc","c1","e2","ef","f8","f5","be","b3","a4","a9","8a","87","90","9d"]
    thirteen07 = ["06","0b","1c","11","32","3f","28","25","6e","63","74","79","5a","57","40","4d"]
    thirteen08 = ["da","d7","c0","cd","ee","e3","f4","f9","b2","bf","a8","a5","86","8b","9c","91"]
    thirteen09 = ["0a","07","10","1d","3e","33","24","29","62","6f","78","75","56","5b","4c","41"]
    thirteen0a = ["61","6c","7b","76","55","58","4f","42","09","04","13","1e","3d","30","27","2a"]
    thirteen0b = ["b1","bc","ab","a6","85","88","9f","92","d9","d4","c3","ce","ed","e0","f7","fa"]
    thirteen0c = ["b7","ba","ad","a0","83","8e","99","94","df","d2","c5","c8","eb","e6","f1","fc"]
    thirteen0d = ["67","6a","7d","70","53","5e","49","44","0f","02","15","18","3b","36","21","2c"]
    thirteen0e = ["0c","01","16","1b","38","35","22","2f","64","69","7e","73","50","5d","4a","47"]
    thirteen0f = ["dc","d1","c6","cb","e8","e5","f2","ff","b4","b9","ae","a3","80","8d","9a","97"]
    ThirteenColumns = [thirteen00,thirteen01,thirteen02,thirteen03,thirteen04,thirteen05,thirteen06,thirteen07,thirteen08,thirteen09,thirteen0a,thirteen0b,thirteen0c,thirteen0d,thirteen0e,thirteen0f]
    fourteen00 = ["00","0e","1c","12","38","36","24","2a","70","7e","6c","62","48","46","54","5a"]
    fourteen01 = ["e0","ee","fc","f2","d8","d6","c4","ca","90","9e","8c","82","a8","a6","b4","ba"]
    fourteen02 = ["db","d5","c7","c9","e3","ed","ff","f1","ab","a5","b7","b9","93","9d","8f","81"]
    fourteen03 = ["3b","35","27","29","03","0d","1f","11","4b","45","57","59","73","7d","6f","61"]
    fourteen04 = ["ad","a3","b1","bf","95","9b","89","87","dd","d3","c1","cf","e5","eb","f9","f7"]
    fourteen05 = ["4d","43","51","5f","75","7b","69","67","3d","33","21","2f","05","0b","19","17"]
    fourteen06 = ["76","78","6a","64","4e","40","52","5c","06","08","1a","14","3e","30","22","2c"]
    fourteen07 = ["96","98","8a","84","ae","a0","b2","bc","e6","e8","fa","f4","de","d0","c2","cc"]
    fourteen08 = ["41","4f","5d","53","79","77","65","6b","31","3f","2d","23","09","07","15","1b"]
    fourteen09 = ["a1","af","bd","b3","99","97","85","8b","d1","df","cd","c3","e9","e7","f5","fb"]
    fourteen0a = ["9a","94","86","88","a2","ac","be","b0","ea","e4","f6","f8","d2","dc","ce","c0"]
    fourteen0b = ["7a","74","66","68","42","4c","5e","50","0a","04","16","18","32","3c","2e","20"]
    fourteen0c = ["ec","e2","f0","fe","d4","da","c8","c6","9c","92","80","8e","a4","aa","b8","b6"]
    fourteen0d = ["0c","02","10","1e","34","3a","28","26","7c","72","60","6e","44","4a","58","56"]
    fourteen0e = ["37","39","2b","25","0f","01","13","1d","47","49","5b","55","7f","71","63","6d"]
    fourteen0f = ["d7","d9","cb","c5","ef","e1","f3","fd","a7","a9","bb","b5","9f","91","83","8d"]
    FourteenColumns = [fourteen00,fourteen01,fourteen02,fourteen03,fourteen04,fourteen05,fourteen06,fourteen07,fourteen08,fourteen09,fourteen0a,fourteen0b,fourteen0c,fourteen0d,fourteen0e,fourteen0f]
    Columns = [[],[],[],[]]
    for i in range(0,4):
        Columns[0].append(block[i][0])
        Columns[1].append(block[i][1]) # splits the block into its 4 columns
        Columns[2].append(block[i][2])
        Columns[3].append(block[i][3])
    NewColumns = [[],[],[],[]]
    GaloisField = [[14,11,13,9],[9,14,11,13],[13,9,14,11],[11,13,9,14]]   # 0e is 14, 0b is 11, 0d is 13 and 09 is 9
    NewvalList = []
    for z in range(0,4):
        for y in range(0,4):
            for x in range(0,4):           # for the 4 items in the column
                if GaloisField[y][x]==9:
                    newval = Columns[z][x]
                    if newval[0].isnumeric():
                        newval1 = int(newval[0])                          # if val is int we can work with it
                    else:
                        newval1 = ord(newval[0]) - 87                      # if not need to tur the hex into is postition, so a = 10 b =11 ect.
                    if newval[1].isnumeric():
                        newval2 = int(newval[1])                          # if val is int we can work with it
                    else:
                        newval2 = ord(newval[1]) - 87                      # if not need to tur the hex into is postition, so a = 10 b =11 ect.
                    Newval = NineColumns[newval1][newval2]
                elif GaloisField[y][x]== 11:
                    newval = Columns[z][x]
                    if newval[0].isnumeric():
                        newval1 = int(newval[0])                          # if val is int we can work with it
                    else:
                        newval1 = ord(newval[0]) - 87                      # if not need to tur the hex into is postition, so a = 10 b =11 ect.
                    if newval[1].isnumeric():
                        newval2 = int(newval[1])                          # if val is int we can work with it
                    else:
                        newval2 = ord(newval[1]) - 87                      # if not need to tur the hex into is postition, so a = 10 b =11 ect.
                    Newval = ElevenColumns[newval1][newval2]
                elif GaloisField[y][x]==13:
                    newval = Columns[z][x]
                    if newval[0].isnumeric():
                        newval1 = int(newval[0])                          # if val is int we can work with it
                    else:
                        newval1 = ord(newval[0]) - 87                      # if not need to tur the hex into is postition, so a = 10 b =11 ect.
                    if newval[1].isnumeric():
                        newval2 = int(newval[1])                          # if val is int we can work with it
                    else:
                        newval2 = ord(newval[1]) - 87                      # if not need to tur the hex into is postition, so a = 10 b =11 ect.
                    Newval = ThirteenColumns[newval1][newval2]
                elif GaloisField[y][x]==14:
                    newval = Columns[z][x]
                    if newval[0].isnumeric():
                        newval1 = int(newval[0])                          # if val is int we can work with it
                    else:
                        newval1 = ord(newval[0]) - 87                      # if not need to tur the hex into is postition, so a = 10 b =11 ect.
                    if newval[1].isnumeric():
                        newval2 = int(newval[1])                          # if val is int we can work with it
                    else:
                        newval2 = ord(newval[1]) - 87                      # if not need to tur the hex into is postition, so a = 10 b =11 ect.
                    Newval = FourteenColumns[newval1][newval2]

                NewvalList.append(Newval)                              # will create a list of the dot product values for the column against the row
            BinaryValue1 = str(bin(int(NewvalList[0], 16))[2:].zfill(8))         #turns all valus to binary
            BinaryValue2 = str(bin(int(NewvalList[1], 16))[2:].zfill(8))
            BinaryValue3 = str(bin(int(NewvalList[2], 16))[2:].zfill(8))
            BinaryValue4 = str(bin(int(NewvalList[3], 16))[2:].zfill(8))
            resultant = ""
            for i in range(0,8):
                if BinaryValue1[i] == BinaryValue2[i]:
                    resultant = resultant+"0"
                else:
                    resultant= resultant+"1"
            resultant2 = ""
            for i in range(0,8):
                if BinaryValue3[i] == BinaryValue4[i]:
                    resultant2 = resultant2+"0"
                else:
                    resultant2= resultant2+"1"
            resultant3 = ""
            for i in range(0,8):
                if resultant[i] == resultant2[i]:
                    resultant3 = resultant3+"0"
                else:
                    resultant3= resultant3+"1"      # performs an Xor of the 4 valus
            NewColumns[z].append(BinToHex(resultant3)) # appends the hex value to the new colmn#
            NewvalList = []
    state = [[],[],[],[]]
    for i in range(0,4):
        state[0].append(NewColumns[i][0])
        state[1].append(NewColumns[i][1]) # splits the block into its 4 columns
        state[2].append(NewColumns[i][2])
        state[3].append(NewColumns[i][3])
    return(state)


def Unblocking(block):
    string = ""
    for row in block:
        for value in row:
            BinaryValue = str(bin(int(value, 16))[2:].zfill(8))
            DecValue = int(BinaryValue, 2)
            letter = chr(DecValue)
            string = string + letter
    return(string)

def AESDecryption(ciphertext, key):
    state = AddRoundKey(ciphertext, key)
    state = InvShiftRows(state)
    state = InvSubBytes(state)
    for i in range(9):
        state = AddRoundKey(state, key)
        state = InvMixColumns(state)
        state = InvShiftRows(state)
        state = InvSubBytes(state)
    state = AddRoundKey(state, key)
    state = Unblocking(state)
    return(state)

