# Mention of the registors
registors = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "FLAGS": "111"}


codes={
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
    "hlt": ["01010", "F"],
}


def decimalTo8bitBinary(num):
    n = int(num)
    s = ''
    while n>0:
        digit = int(n%2)
        if digit<2:
            s += str(digit)
        else:
            s += chr(ord('A') + digit - 2)
        n //= 2
    s = s[::-1]
    if len(s) < 8:
        s = "0" * (8 - len(s)) + str(s)
    return str(s)


def printTypeA(opcode, reg1, reg2, reg3):
    print(f"{codes[opcode][0]}00{registors[reg1]}{registors[reg2]}{registors[reg3]}")


def printTypeB(opcode, reg1, value):
    print(f"{codes[opcode[0]]}{registors[reg1]}{decimalTo8bitBinary(value)}")


def printTypeC(opcode, reg1, reg2):
    print(f"{codes[opcode][0]}00000{registors[reg1]}{registors[reg2]}")


def printTypeD(opcode, reg1, address):
    print(f"{codes[opcode][0]}{registors[reg1]}{address}")


def printTypeE(opcode, address):
    print(f"{codes[opcode][0]}000{address}")


def printTypeF(opcode, reg1, reg2, reg3):
    print(f"{codes[opcode][0]}00000000000")


variables=[]
variablecount=0
temp=[]
temp1=[]

# Main program
# if __name__== "__main__":
#     print("Welcome to the COASS assembler")
#     with open("practiseInput.txt", "r") as file:
#         # data = file.readline()
#         # print(data)
#         data=file.read()
#         temp=data.split("\n")
#         print(temp)

#     if temp

# while True:
#     try:
#         line = input()
#         if line.strip != '':
#             temp.append(line)
#         temp1.append(line)
#     except EOFError:
#         break
        


# Main program
if __name__== "__main__":
    print("Welcome to the assembler!")
    with open("practiseInput.txt", "r") as file:
        data = file.read().split("\n")
    
    data.pop()
    for i in data:
        temp = list(i.split())
        if temp[0]=='var':
            variables.append(temp[1])
            variablecount+=1
            continue
        if codes[temp[0]][1] == 'A':
            printTypeA(temp[0], temp[1], temp[2], temp[3])
        if codes[temp[0]][1] == 'B':
            printTypeB(temp[0], temp[1], temp[2], temp[3])
        if codes[temp[0]][1] == 'C':
            printTypeC(temp[0], temp[1], temp[2], temp[3])
        if codes[temp[0]][1] == 'D':
            printTypeD(temp[0], temp[1], temp[2], temp[3])
        if codes[temp[0]][1] == 'E':
            printTypeE(temp[0], temp[1], temp[2], temp[3])
        if codes[temp[0]][1] == 'F':
            printTypeF(temp[0], temp[1], temp[2], temp[3])
   
    # s = 'mul'
    # print(codes[s][1])
