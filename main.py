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
codes={
    "add": ["10000", "A"],
    "sub": ["10001", "A"],
    "mov": ["10010", "B"],
    "mov": ["10011", "C"],
    "ld": ["10100", "D"],
    "st": ["10001", "D"],
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
    "hlt": ["01010", "F"],
}


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


def printTypeA(opcode, reg1, reg2, reg3):
    print(f"{codes[opcode][0]}00{registors[reg1]}{registors[reg2]}{registors[reg3]}")


def printTypeB(opcode, reg1, value):
    n = int(value[1::])
    if (n <= 255 and n >= 0):
        print(f"{codes[opcode][0]}{registors[reg1]}{decimalTo8bitBinary(value[1::])}")
    else:
        print("\nERROR\nIllegal Immediate Value used!")
        exit()


def printTypeC(opcode, reg1, reg2):
    print(f"{codes[opcode][0]}00000{registors[reg1]}{registors[reg2]}")


def printTypeD(opcode, reg1, address):
    print(f"{codes[opcode][0]}{registors[reg1]}{address}")


def printTypeE(opcode, address):
    print(f"{codes[opcode][0]}000{address}")


def printTypeF(opcode):
    print(f"{codes[opcode][0]}00000000000")


variables=[]
variablecount=0
track = 0

# Main program
if __name__== "__main__":
    print("Welcome to the Assembler!")
    with open("practiseInput.txt", "r") as file:
        data = file.read().split("\n")
    data.pop()

    print("\nMachine Code:-")
    try:
        for i in data:
            temp = list(i.split())
            # print(temp)
            if temp[0] == 'var':
                variables.append(temp[1])
                variablecount += 1
                track += 1
                continue

            if temp[0] == "mov":
                if (temp[2][0]) == "$":
                    printTypeB(temp[0], temp[1], temp[2])
                    track += 1
                    continue
                else:
                    printTypeC(temp[0], temp[1], temp[2])
                    track += 1
                    continue

            if codes[temp[0]][1] == 'A':
                printTypeA(temp[0], temp[1], temp[2], temp[3])
                track += 1

            if codes[temp[0]][1] == 'B':
                printTypeB(temp[0], temp[1], temp[2])
                track += 1

            if codes[temp[0]][1] == 'C':
                printTypeC(temp[0], temp[1], temp[2])
                track += 1

            if (codes[temp[0]][1] == 'D'):
                if (temp[2] in variables):
                    printTypeD(temp[0], temp[1], temp[2])
                    track += 1
                else:
                    print("\nERROR\nUndefined Varaible Used!")
                    exit()

            if codes[temp[0]][1] == 'E':
                printTypeE(temp[0], temp[1])
                track += 1

            if codes[temp[0]][1] == 'F':
                printTypeF(temp[0])
                track += 1
                break

        if track != len(data):
            print("\nERROR\nLast Instruction is required to be HLT")
            exit()
        if temp != ['hlt']:
            print("\nERROR\nHLT Instruction Missing!")
        else:
            print(f"\nNumber of Variables: {variablecount}")
            print("Variables:-", end = " ")
            for i in variables:
                print(i, end = " ")
            print()
    except KeyError:
        print("\nERROR\nThe given Instructions/Registors are not VALID!")
        exit()
    except:
        print("\nERROR\nGeneral Syntax Error")
