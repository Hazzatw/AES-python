
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

def SubBytes(block):
    Newblock = [[],[],[],[]]
         # S-Box
     #	      00   01   02   03   04   05   06   07   08   09   0a   0b   0c   0d   0e   0f
    R00 =   ["63","7c","77","7b","f2","6b","6f","c5","30","01","67","2b","fe","d7","ab","76"]
    R10 =   ["ca","82","c9","7d","fa","59","47","f0","ad","d4","a2","af","9c","a4","72","c0"]
    R20	=   ["b7","fd","93","26","36","3f","f7","cc","34","a5","e5","f1","71","d8","31","15"]
    R30	=   ["04","c7","23","c3","18","96","05","9a","07","12","80","e2","eb","27","b2","75"]
    R40	=   ["09","83","2c","1a","1b","6e","5a","a0","52","3b","d6","b3","29","e3","2f","84"]
    R50	=   ["53","d1","00","ed","20","fc","b1","5b","6a","cb","be","39","4a","4c","58","cf"]
    R60	=   ["d0","ef","aa","fb","43","4d","33","85","45","f9","02","7f","50","3c","9f","a8"]
    R70	=   ["51","a3","40","8f","92","9d","38","f5","bc","b6","da","21","10","ff","f3","d2"]
    R80 =	["cd","0c","13","ec","5f","97","44","17","c4","a7","7e","3d","64","5d","19","73"]
    R90	=   ["60","81","4f","dc","22","2a","90","88","46","ee","b8","14","de","5e","0b","db"]
    Ra0	=   ["e0","32","3a","0a","49","06","24","5c","c2","d3","ac","62","91","95","e4","79"]
    Rb0	=   ["e7","c8","37","6d","8d","d5","4e","a9","6c","56","f4","ea","65","7a","ae","08"]
    Rc0	=   ["ba","78","25","2e","1c","a6","b4","c6","e8","dd","74","1f","4b","bd","8b","8a"]
    Rd0	=   ["70","3e","b5","66","48","03","f6","0e","61","35","57","b9","86","c1","1d","9e"]
    Re0	=   ["e1","f8","98","11","69","d9","8e","94","9b","1e","87","e9","ce","55","28","df"]
    Rf0 =   ["8c","a1","89","0d","bf","e6","42","68","41","99","2d","0f","b0","54","bb","16"]
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


def ShiftRows(block):
    Newblock = [[],[],[],[]]     # creats empty new block
    for value in block[0]:
        (Newblock[0]).append(value)      # first row just copies each value from origonal bloack
    for i in range(1,4):
        Newblock[1].append((block[1])[i])     # second  row copies the last 3 values
    Newblock[1].append(block[1][0])             #  then copies the first
    for i in range(2,4):
        Newblock[2].append((block[2])[i])           # third row copies the last two
        print(i)
    for i in range(0,2):
        Newblock[2].append((block[2])[i])            # then the first two
        print(i)
    Newblock[3].append(block[3][3])           # forth row copies the last value
    for i in range(0,3):
        Newblock[3].append(block[3][i])        # fourth row copies the first 3
    return(Newblock)   # returns Shift Rows


def AddRoundKey(block,subkey):
    NewState = [[],[],[],[]]
    for i in range(0,4):     # for the four rows in each block
        for x in range(0,4):      # for the four items in each row
            Value1 = block[i][x] # block row x item i
            Value2 = subkey[i][x]   # subkey row x item i
            BinaryValue1 = str(bin(int(Value1, 16))[2:].zfill(8))  # turns the hex values into binary
            BinaryValue2 = str(bin(int(Value2, 16))[2:].zfill(8))
            resultant = int(BinaryValue1, 2)^int(BinaryValue2,2)# performs a logic bitwise XOR
            resultant = str(int(bin(resultant)[2:]))      # turs answer into binary from decimal
            for zeros in range(8-len(resultant)):  # padds out zeros, if binary value is not 8 bit
                resultant = "0"+resultant
            resultant = BinToHex(resultant)   # put through Binary to hex function
            NewState[i].append(resultant)
    return (NewState)

def MixColumns(block):

    Two0 = ["00","02","04","06","08","0a","0c","0e","10","12","14","16","18","1a","1c","1e"]   #  look up table for galois multiplications by 2 ['d4', 78, 51, 'ae']
    Two1 = ["20","22","24","26","28","2a","2c","2e","30","32","34","36","38","3a","3c","3e"]
    Two2 = ["40","42","44","46","48","4a","4c","4e","50","52","54","56","58","5a","5c","5e"]
    Two3 = ["60","62","64","66","68","6a","6c","6e","70","72","74","76","78","7a","7c","7e"]
    Two4 = ["80","82","84","86","88","8a","8c","8e","90","92","94","96","98","9a","9c","9e"]
    Two5 = ["a0","a2","a4","a6","a8","aa","ac","ae","b0","b2","b4","b6","b8","ba","bc","be"]
    Two6 = ["c0","c2","c4","c6","c8","ca","cc","ce","d0","d2","d4","d6","d8","da","dc","de"]
    Two7 = ["e0","e2","e4","e6","e8","ea","ec","ee","f0","f2","f4","f6","f8","fa","fc","fe"]
    Two8 = ["1b","19","1f","1d","13","11","17","15","0b","09","0f","0d","03","01","07","05"]
    Two9 = ["3b","39","3f","3d","33","31","37","35","2b","29","2f","2d","23","21","27","25"]
    Twoa = ["5b","59","5f","5d","53","51","57","55","4b","49","4f","4d","43","41","47","45"]
    Twob = ["7b","79","7f","7d","73","71","77","75","6b","69","6f","6d","63","61","67","65"]
    Twoc = ["9b","99","9f","9d","93","91","97","95","8b","89","8f","8d","83","81","87","85"]
    Twod = ["bb","b9","bf","bd","b3","b1","b7","b5","ab","a9","af","ad","a3","a1","a7","a5"]
    Twoe = ["db","d9","df","dd","d3","d1","d7","d5","cb","c9","cf","cd","c3","c1","c7","c5"]
    Twof = ["fb","f9","ff","fd","f3","f1","f7","f5","eb","e9","ef","ed","e3","e1","e7","e5"]
    TwoColumns = [Two0,Two1,Two2,Two3,Two4,Two5,Two6,Two7,Two8,Two9,Twoa,Twob,Twoc,Twod,Twoe,Twof]

    Three0 = ["00","03","06","05","0c","0f","0a","09","18","1b","1e","1d","14","17","12","11"]
    Three1 = ["30","33","36","35","3c","3f","3a","39","28","2b","2e","2d","24","27","22","21"]
    Three2 = ["60","63","66","65","6c","6f","6a","69","78","7b","7e","7d","74","77","72","71"]
    Three3 = ["50","53","56","55","5c","5f","5a","59","48","4b","4e","4d","44","47","42","41"]
    Three4 = ["c0","c3","c6","c5","cc","cf","ca","c9","d8","db","de","dd","d4","d7","d2","d1"]
    Three5 = ["f0","f3","f6","f5","fc","ff","fa","f9","e8","eb","ee","ed","e4","e7","e2","e1"]
    Three6 = ["a0","a3","a6","a5","ac","af","aa","a9","b8","bb","be","bd","b4","b7","b2","b1"]
    Three7 = ["90","93","96","95","9c","9f","9a","99","88","8b","8e","8d","84","87","82","81"]
    Three8 = ["9b","98","9d","9e","97","94","91","92","83","80","85","86","8f","8c","89","8a"]
    Three9 = ["ab","a8","ad","ae","a7","a4","a1","a2","b3","b0","b5","b6","bf","bc","b9","ba"]
    Threea = ["fb","f8","fd","fe","f7","f4","f1","f2","e3","e0","e5","e6","ef","ec","e9","ea"]
    Threeb = ["cb","c8","cd","ce","c7","c4","c1","c2","d3","d0","d5","d6","df","dc","d9","da"]
    Threec = ["5b","58","5d","5e","57","54","51","52","43","40","45","46","4f","4c","49","4a"]
    Threed = ["6b","68","6d","6e","67","64","61","62","73","70","75","76","7f","7c","79","7a"]
    Threee = ["3b","38","3d","3e","37","34","31","32","23","20","25","26","2f","2c","29","2a"]
    Threef = ["0b","08","0d","0e","07","04","01","02","13","10","15","16","1f","1c","19","1a"]
    ThreeColumns = [Three0,Three1,Three2,Three3,Three4,Three5,Three6,Three7,Three8,Three9,Threea,Threeb,Threec,Threed,Threee,Threef]
    Columns = [[],[],[],[]]
    for i in range(0,4):
        Columns[0].append(block[i][0])
        Columns[1].append(block[i][1]) # splits the block into its 4 columns
        Columns[2].append(block[i][2])
        Columns[3].append(block[i][3])
    NewColumns = [[],[],[],[]]
    GaloisField = [[2,3,1,1],[1,2,3,1],[1,1,2,3,],[3,1,1,2]]   # standard  key for AES
    NewvalList = []
    for z in range(0,4):
        for y in range(0,4):
            for x in range(0,4):           # for the 4 items in the column
                if GaloisField[y][x]== 1:           # if the corresponding item on the gallois row is 1 it stays the same
                    Newval = Columns[z][x]
                elif GaloisField[y][x]== 2:
                    newval = Columns[z][x]
                    if newval[0].isnumeric():
                        newval1 = int(newval[0])                          # if val is int we can work with it
                    else:
                        newval1 = ord(newval[0]) - 87                      # if not need to tur the hex into is postition, so a = 10 b =11 ect.
                    if newval[1].isnumeric():
                        newval2 = int(newval[1])                          # if val is int we can work with it
                    else:
                        newval2 = ord(newval[1]) - 87                      # if not need to tur the hex into is postition, so a = 10 b =11 ect.
                    Newval = TwoColumns[newval1][newval2]
                elif GaloisField[y][x]==3:
                    newval = Columns[z][x]
                    if newval[0].isnumeric():
                        newval1 = int(newval[0])                          # if val is int we can work with it
                    else:
                        newval1 = ord(newval[0]) - 87                      # if not need to tur the hex into is postition, so a = 10 b =11 ect.
                    if newval[1].isnumeric():
                        newval2 = int(newval[1])                          # if val is int we can work with it
                    else:
                        newval2 = ord(newval[1]) - 87                      # if not need to tur the hex into is postition, so a = 10 b =11 ect.
                    Newval = ThreeColumns[newval1][newval2]

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


def Blocking(Plaintext, Key): # turns the plaintext and key into usabale 4*4 blocks of hex vavlues
    Newlist = []
    PandK = [Plaintext, Key]
    for PorK in PandK:
        for letter in PorK:
            letter = bin(ord(letter))[2:].zfill(8)
            letter = BinToHex(letter)
            Newlist.append(letter)
    Plaintext = [[],[],[],[]]
    for i in range(0,16):
        if i<4:
            Plaintext[0].append(Newlist[i])
        elif i<8:
            Plaintext[1].append(Newlist[i])
        elif i<12:
            Plaintext[2].append(Newlist[i])
        else:
            Plaintext[3].append(Newlist[i])
    Key = [[],[],[],[]]
    for i in range(16,32):
        if i<20:
            Key[0].append(Newlist[i])
        elif i<24:
            Key[1].append(Newlist[i])
        elif i<28:
            Key[2].append(Newlist[i])
        else:
            Key[3].append(Newlist[i])
    return(Plaintext, Key)





def AESEncrypt(Block, Key):
    Block, Key = Blocking(Block, Key)
    State = AddRoundKey(Block,Key)      # runs addrounf key once
    for i in range(9):
        State = SubBytes(State)
        State = ShiftRows(State)         # runs all 4 main processes 9 times
        State = MixColumns(State)
        State = AddRoundKey(State, Key)

    State = SubBytes(State)
    State = ShiftRows(State)            # runs finale three
    State = AddRoundKey(State,Key)
    return State
                                        # returns ciphered state


/Users/harrywalmsley/AES-python/AESEncrption.py