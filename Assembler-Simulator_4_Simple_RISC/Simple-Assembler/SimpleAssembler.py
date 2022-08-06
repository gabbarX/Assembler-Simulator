import sys

# Mention of the Registors
registors = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "FLAGS": "111"}

#Mention of Instructions
codes = {   
    "add": ["10000", "A"],
    "sub": ["10001", "A"],
    "mov": ["10010", "B"],
    "mov": ["10011", "C"],
    "ld": ["10100", "D"],
    "st": ["10101", "D"],
    "mul": ["10110", "A"],
    "div": ["10111", "C"],
    "rs": ["11000", "B"],
    "ls": ["11001", "B"],
    "xor": ["11010", "A"],
    "or": ["11011", "A"],
    "and": ["11100", "A"],
    "not": ["11101", "C"],
    "cmp": ["11110", "C"],
    "jmp": ["11111", "E"],
    "jlt": ["01100", "E"],
    "jgt": ["01101", "E"],
    "je": ["01111", "E"],
    "addf": ["00000", "A"],
    "subf": ["00001", "A"],
    "movf": ["00010", "B"],
    "hlt": ["01010", "F"]}

#global Varaibles
errorpresent = False
errorcount = 0
variablecount = 0
track = 0
label = {}
variables = {}
code = []
initialcode = []
temp = []
count = 0
result = []

#Functions
def decimalTo8bitBinary(num):
    n = int(num)
    ns = ""
    while n>0:
        ns += str(n%2)
        n = n//2
    nf = ns[::-1]
    if len(nf) < 8:
        nf = "0" * (8 - len(nf)) + str(nf)
    return str(nf)

#storing the memory address of the variable and labels in a dictionary
def decimalToBinary(num):
    n = int(num)
    ns = ""
    while n>0:
        ns += str(n%2)
        n = n//2
    nf = ns[::-1]
    return str(nf)

def binaryToDecimal(binary):
    decimal = 0
    j = 0
    for i in range(len(binary)):
        if(int(binary[i]) == 0):
            decimal += 0
            j = j + 1
        else:
            decimal += 2**j
            j = j + 1
    return decimal

def decimalbinaryToDecimal(binary):
    decimal = 0
    j = -1
    for i in range(len(binary)):
        if(int(binary[i]) == 0):
            decimal += 0
            j = j - 1
        else:
            decimal += 2**j
            j = j - 1
    return decimal

def BinarytoFloatingpoint(Instruction):
    l = list(str(Instruction))
    a = l[8:]
    exp = a[0] + a[1] + a[2]
    mantissa = a[3] + a[4] + a[5] + a[6] + a[7]
    decimalexp = binaryToDecimal(exp)
    mantissaexp = decimalbinaryToDecimal(mantissa)
    ans = (2**decimalexp - 3)*(1 + mantissaexp)
    return ans

def floattobinary(number, places):
	whole, dec = str(number).split(".")
	whole = int(whole)
	dec = int (dec)
	res = bin(whole).lstrip("0b") + "."
	for x in range(places):
		whole, dec = str((decimal_converter(dec)) * 2).split(".")
		dec = int(dec)
		res += whole
	return res

def decimal_converter(num):
	while num > 1:
		num /= 10
	return num

def decimalToBinaryforexp(num):
    n = int(num)
    ns = ""
    while n>0:
        ns += str(n%2)
        n = n//2
    nf = ns[::-1]
    if len(nf) < 3:
        nf = "0" * (3 - len(nf)) + str(nf)
    return str(nf)

def movf(num):
    n = num
    count = 0
    while(n > 2):
        count += 1
        n = n/2
    inn = str(int(n))
    linn = len(inn)
    p = len(str(n)) - linn - 1
    return(count, floattobinary(n, p))

def storeAddress():
    global count
    for i in range(0, len(initialcode)):
        command=initialcode[i].strip().split()
        if len(command)==0:
            continue
        if command[0]=='var':
            if(len(command)==1):
                continue
            else:
                variables[command[1]]=None
        else:
            if ':' in command[0]:
                code.append(command[1:])
                temp.append(command)
                count+=1
            else:
                code.append(command)
                temp.append(command)
                count+=1

    for i in variables:
        variables[i] = decimalTo8bitBinary(count)
        count += 1

    for i in range(0,len(temp)):
        if ':' in temp[i][0]:
            labelname=temp[i][0]
            label[labelname.rstrip(':')]=decimalTo8bitBinary(i)

#printing memory addresses
def memoryAddressofVar(var):
    return variables[var]

def memoryAddressofLabel(key):
    return label[key]

#Flag Check
def flagcheck(command):
    # print(command)
    if command[0]=='mov' and (command[1]=='FLAGS' and command[2]!='FLAGS'):
        # print(command[0])
        return True
    else:
        return False

#printing Functions according to the Types
def printTypeA(opcode, reg1, reg2, reg3):
    ns = (f"{codes[opcode][0]}00{registors[reg1]}{registors[reg2]}{registors[reg3]}")
    return ns

def printTypeB(opcode, reg1, value):
    temp=value.split('$').pop()
    if opcode == "mov":
        ns = (f"10010{registors[reg1]}{decimalTo8bitBinary(temp)}")
        return ns
    else:
        ns = (f"{codes[opcode][0]}{registors[reg1]}{decimalTo8bitBinary(temp)}")
        return ns

def printTypeC(opcode, reg1, reg2):
    ns = (f"{codes[opcode][0]}00000{registors[reg1]}{registors[reg2]}")
    return ns

def printTypeD(opcode, reg1, var):
    ns = (f"{codes[opcode][0]}{registors[reg1]}{memoryAddressofVar(var)}")
    return ns

def printTypeE(opcode, label):
    ns = (f"{codes[opcode][0]}000{memoryAddressofLabel(label)}")
    return ns

def printTypeF(opcode):
    ns = (f"{codes[opcode][0]}00000000000")
    return ns

# Main program
if __name__== "__main__":


    for line in sys.stdin:
        if "" == line.rstrip():
            break
        initialcode.append(line.strip())

    storeAddress()
    check = True
    for temp in code:
        if "FLAGS" in temp:
            check = flagcheck(temp)

    if check is True:
        try:
            for temp in code:
                if temp[0] == 'var':
                    variablecount += 1
                    track += 1
                    continue

                if temp[0] == "mov":
                    if (temp[2][0]) == "$":
                        n = int(temp[2][1::])
                        if (n <= 255 and n >= 0):
                            result.append(printTypeB(temp[0], temp[1], temp[2][1::]))
                        else:
                            print("ERROR: Illegal Immediate Value used at Line:",len(variables) + code.index(temp)+1)
                            errorcount += 1
                            quit()
                        track += 1
                        continue
                    else:
                        result.append(printTypeC(temp[0], temp[1], temp[2]))
                        track += 1
                        continue
                elif temp[0] == "movf":
                    if (temp[2][0]) == "$":
                        n = float(temp[2][1::])
                        if (n <= 246 and n >= 0):
                            l = list((movf(n)[1]))
                            a = l[2:]      
                            la = len(a)
                            ans = ""
                            while(la < 5):
                                a.append("0")
                                la += 1
                            for i in a:
                                ans += str(i)
                            result.append(("00010"+str(registors[temp[1]])+str(decimalToBinaryforexp(movf(n)[0] + 3))+str(ans)))

                        else:
                            print("ERROR: Illegal Immediate Value used at Line:",len(variables) + code.index(temp)+1)
                            errorcount += 1
                            quit()
                        track += 1
                        continue
                    else:
                        result.append(printTypeC(temp[0], temp[1], temp[2]))
                        track += 1
                        continue

                if codes[temp[0]][1] == 'A':
                    result.append(printTypeA(temp[0], temp[1], temp[2], temp[3]))
                    track += 1

                if codes[temp[0]][1] == 'B':
                    result.append(printTypeB(temp[0], temp[1], temp[2]))
                    track += 1

                if codes[temp[0]][1] == 'C':
                    result.append(printTypeC(temp[0], temp[1], temp[2]))
                    track += 1

                if (codes[temp[0]][1] == 'D'):
                    if (temp[2] in variables.keys()):
                        result.append(printTypeD(temp[0], temp[1], temp[2]))
                        track += 1
                        
                    else:
                        print("ERROR: Undefined Varaible Used at Line ", len(variables) + code.index(temp)+1)
                        errorpresent = True
                        errorcount += 1
                        exit()

                if codes[temp[0]][1] == 'E':
                    if (temp[1] in label.keys()):
                        result.append(printTypeE(temp[0], temp[1]))
                        track += 1

                    else:
                        print("ERROR: Undefined Label Used at Line ", len(variables) + code.index(temp)+1)
                        errorpresent = True
                        errorcount += 1
                        exit()

                if codes[temp[0]][1] == 'F':
                    result.append(printTypeF(temp[0]))
                    track += 1
                    break

            if track != len(code):
                print("ERROR: Last Instruction is required to be HLT")
                errorpresent = True
                errorcount += 1
                exit()

            temp = initialcode[-1]
            if (":" in temp):
                temp2 = list(temp.split())
                hltcheck = temp2[1]
            else:
                hltcheck = temp
            if hltcheck != 'hlt':
                print("ERROR: HLT Instruction Missing or Misplaced!")
                errorpresent = True
                errorcount += 1

        except KeyError:
            print("ERROR: The given Instructions/Registors are not VALID!")
            errorpresent = True
            errorcount += 1
            exit()

        except:
            if (errorcount == 0):
                print("ERROR: General Syntax Error")
                errorpresent = True
            else:
                exit()

    else:
        print("Flag Error at line: ", len(variables) + code.index(temp))
        errorpresent = True
        exit()

if errorpresent is False:
    for i in result:
        print(i)
