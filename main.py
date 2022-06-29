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
    pass


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


# Main program
if __name__== "__main__":
    print("Welcome to the COASS assembler")
    with open("practiseInput.txt", "r") as file:
        data = file.read().split("\n")

for i in data:
    curr = list(i.split())
    print(curr)

# Main program
if __name__== "__main__":
    print("Welcome to the assembler!")
    l = ["mul", "R3", "R1", "R2"]
    printTypeA(l[0], l[1], l[2], l[3])