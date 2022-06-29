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


def printTypeA(opcode, reg1, reg2, reg3):
    pass


def printTypeB(opcode, reg1, reg2, reg3):
    pass


def printTypeC(opcode, reg1, reg2, reg3):
    pass


def printTypeD(opcode, reg1, reg2, reg3):
    pass


def printTypeE(opcode, reg1, reg2, reg3):
    pass


def printTypeF(opcode, reg1, reg2, reg3):
    pass


# Main program
if __name__== "__main__":
    print("Welcome to the COASS assembler")
    with open("practiseInput.txt", "r") as file:
        data = file.read().split("\n")

for i in data:
    curr = list(i.split())
    print(curr)
