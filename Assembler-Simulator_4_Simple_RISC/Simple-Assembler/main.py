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
    "st": ["10001", "D"],
    "mul": ["10110", "A"],
    "div": ["10111", "C"],
    "rs": ["11000", ""],
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
    "hlt": ["01010", "F"]}


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
def storeAddress():
    global count
    for i in range(0,len(initialcode)):
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
        variables[i]=decimalTo8bitBinary(count)
        count+=1

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
    if command[0]=='mov' and command[1]!='FLAGS' and command[2]=='FLAGS':
        return True
    else:
        return False


#printing Functions according to the Types
def printTypeA(opcode, reg1, reg2, reg3):
    ns = (f"{codes[opcode][0]}00{registors[reg1]}{registors[reg2]}{registors[reg3]}")
    return ns


def printTypeB(opcode, reg1, value):
    n = int(value[1::])
    if (n <= 255 and n >= 0):
        ns = (f"{codes[opcode][0]}{registors[reg1]}{decimalTo8bitBinary(value[1::])}")
        return ns
    else:
        print("\nERROR\nIllegal Immediate Value used!")
        quit()


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


variablecount=0
track = 0
label = {}
variables = {}
code=[]
initialcode=[]
temp=[]
count=0
result = []
error = []

# Main program
if __name__== "__main__":
    with open("practiseInput.txt", "r") as file:
        data = file.read().split("\n")
        for i in data:
            if (len(i) != 0):
                initialcode.append(i)
    
    storeAddress()

    for temp in code:
        if "FLAGS" in temp:
            check = flagcheck(temp)
        else:
            check = True

    if check is True:
        try:
            for temp in code:
                if temp[0] == 'var':
                    variablecount += 1
                    track += 1
                    continue

                if temp[0] == "mov":
                    if (temp[2][0]) == "$":
                        result.append(printTypeB(temp[0], temp[1], temp[2]))
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
                        print("\nERROR\nUndefined Varaible Used!")
                        exit()

                if codes[temp[0]][1] == 'E':
                    if (temp[1] in label.keys()):
                        result.append(printTypeE(temp[0], temp[1]))
                        track += 1
                    else:
                        print("\nERROR\nUndefined Label Used!")
                        exit()
                if codes[temp[0]][1] == 'F':
                    result.append(printTypeF(temp[0]))
                    track += 1
                    break

            for i in result:
                print(i)

            if track != len(code):
                print("\nERROR\nLast Instruction is required to be HLT")
                exit()
            if code[-1] != ["hlt"]:
                print("\nERROR\nHLT Instruction Missing!")
        except KeyError:
            print("\nERROR\nThe given Instructions/Registors are not VALID!")
            exit()
        except:
            print("\nERROR\nGeneral Syntax Error")

    else:
        print("\nERROR\nFlag Error")
        exit()
