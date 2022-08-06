import sys

# Mentions of Registors
regs = {"000": "0000000000000000",
        "001": "0000000000000000",
        "010": "0000000000000000",
        "011": "0000000000000000",
        "100": "0000000000000000",
        "101": "0000000000000000",
        "110": "0000000000000000",
        "111": "0000000000000000"}

memory_address = []
programCounter = 0
cycle_number = 0

#Utility Functions
def memoryDump():
    for i in memory_address:
        print(i)

# def memoryDump(track):
#     for i in range(track, 256):
#         for i in regs.values():
#             print(i, end = " ")
#         print()


def binary2decimal(num):
    n = str(num)[::-1]
    count = 0
    for i in range(len(n)):
        count += int(n[i])*(2**int(i))
    return count


def decimal2binary(num):
    n = int(num)
    ns = ""
    while n>0:
        ns += str(n%2)
        n = n//2
    nf = ns[::-1]
    if len(nf) < 16:
        nf = "0" * (16 - len(nf)) + str(nf)
    return str(nf)


def getbin(num):
    n = int(num)
    ns = ""
    while n>0:
        ns += str(n%2)
        n = n//2
    nf = ns[::-1]
    return(nf)


def givepc(value):
    x = getbin(value)
    if len(x) < 8:
        x = "0" * (8 - len(x)) + str(x)
    return str(x)


def printline():
    print(givepc(programCounter), end=' ')
    for i in regs:
        print(regs[i], end=' ')
    print()


#Functions for Instruction
def add(line):
    global programCounter
    reg1 = binary2decimal(regs[line[7:10]])
    reg2 = binary2decimal(regs[line[10:13]])
    reg3 = line[13:]
    reg4 = reg1 + reg2

    if reg4 > 256 or reg4 < 0:
        regs["111"] = "0000000000001000"
    else:
        regs["111"] = "0000000000000000"

    regs[reg3] = decimal2binary(reg4)
    printline()
    programCounter += 1


def sub(line):
    global programCounter
    reg1 = binary2decimal(regs[line[7:10]])
    reg2 = binary2decimal(regs[line[10:13]])
    reg3 = line[13:]
    reg4 = reg1 - reg2

    if reg4 > 256 or reg4 < 0:
        regs["111"] = "0000000000001000"
    else:
        regs["111"] = "0000000000000000"

    regs[reg3] = decimal2binary(reg4)
    printline()
    programCounter += 1


def movimm(line):
    global programCounter
    reg = line[5:8]
    value = binary2decimal(line[8:])
    regs[reg] = decimal2binary(value)
    printline()
    programCounter += 1


def movreg(line):
    global programCounter
    regs[line[13:]]=regs[line[10:13]]
    # print("hehe",line[10:13], line[13:])
    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def load(line):
    global programCounter
    value = binary2decimal(line[8:])
    regs[line[5:8]] = memory_address[value]
    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def store(line):
    global programCounter
    string = line[8:]
    value = int(string, 2)
    memory_address[value] = regs[line[5:8]]
    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def mul(line):
    global programCounter
    reg1 = binary2decimal(regs[line[7:10]])
    reg2 = binary2decimal(regs[line[10:13]])
    reg3 = line[13:]
    reg4 = reg2 * reg1

    if reg4 > 256 or reg4 < 0:
        regs["111"] = "0000000000001000"
    else:
        regs["111"] = "0000000000000000"

    regs[reg3] = decimal2binary(reg4)
    printline()
    programCounter += 1


def div(line):
    global programCounter
    reg1 = binary2decimal(regs[line[10:13]])
    reg2 = binary2decimal(regs[line[13:]])

    regs["000"] = decimal2binary(reg1 / reg2)
    regs["001"] = decimal2binary(reg1 % reg2)
    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def rs(line):
    global programCounter
    reg = line[5:8]
    value = line[8:]
    regValue = binary2decimal(regs[reg])

    regs[reg] = decimal2binary(regValue >> value)

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def ls(line):
    global programCounter
    reg = line[5:8]
    value = line[8:]
    regValue = binary2decimal(regs[reg])

    regs[reg] = decimal2binary(regValue << value)

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def xorop(line):
    global programCounter
    reg1 = line[7:10]
    reg2 = decimal2binary(line[10:13])
    reg3 = decimal2binary(line[13:])

    regs[reg1] = decimal2binary(reg2 ^ reg3)

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def orop(line):
    global programCounter
    reg1 = line[7:10]
    reg2 = decimal2binary(line[10:13])
    reg3 = decimal2binary(line[13:])

    regs[reg1] = decimal2binary(reg2 | reg3)

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def andop(line):
    global programCounter
    reg1 = line[7:10]
    reg2 = decimal2binary(line[10:13])
    reg3 = decimal2binary(line[13:])

    regs[reg1] = decimal2binary(reg2 & reg3)

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def notop(line):
    global programCounter
    reg1 = line[10:13]
    reg2 = decimal2binary(line[13:])
    regs[reg1] = decimal2binary(~reg2)

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def compare(line):
    global programCounter
    reg1 = binary2decimal(regs[line[10:13]])
    reg2 = binary2decimal(regs[line[13:]])

    if reg1 < reg2:
        regs["111"] = "0000000000000100"
    if reg1 > reg2:
        regs["111"] = "0000000000000010"
    if reg1 == reg2:
        regs["111"] = "0000000000000001"
    printline()
    programCounter += 1


def jmp(line):
    global programCounter
    regs["111"] = "0000000000000000"
    printline()
    programCounter = binary2decimal(line[8:])


def jlt(line):
    global programCounter
    if regs["111"] == "0000000000000100":
        printline()
        programCounter = binary2decimal(line[8:])
        return

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def jgt(line):
    global programCounter
    if regs["111"] == "0000000000000010":
        printline()
        programCounter = binary2decimal(line[8:])
        return

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def je(line):
    global programCounter
    if regs["111"] == "0000000000000001":
        printline()
        programCounter = binary2decimal(line[8:])
        return

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def hlt(line):
    global programCounter
    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def perform(line):
    global programCounter
    global cycle_number

    opcode=line[:5]
    if opcode == "00000":
        for i in regs.values():
            print(i, end = " ")
        print()
    if opcode == "10000":
        add(line)
    elif opcode == "10001":
        sub(line)
    elif opcode == "10010":
        movimm(line)
    elif opcode == "10011":
        movreg(line)
    elif opcode == "10100":
        load(line)
    elif opcode == "10101":
        store(line)
    elif opcode == "10110":
        mul(line)
    elif opcode == "10111":
        div(line)
    elif opcode == "11000":
        rs(line)
    elif opcode == "11001":
        ls(line)
    elif opcode == "11010":
        xorop(line)
    elif opcode == "11011":
        orop(line)
    elif opcode == "11100":
        andop(line)
    elif opcode == "11101":
        notop(line)
    elif opcode == "11110":
        compare(line)
    elif opcode == "11111":
        jmp(line)
    elif opcode == "01100":
        jlt(line)
    elif opcode == "01101":
        jgt(line)
    elif opcode == "01111":
        je(line)
    elif opcode == "01010":
        hlt(line)


if __name__ == '__main__':
    track = 0
    commands=[]
    #Taking Input
    for line in sys.stdin:
        if "" == line.rstrip():
            break
        commands.append(line.strip())

    for i in range(0,256):
        if i < len(commands):
            # print("hehe",commands)
            memory_address.append(commands[i])
        if i >= len(commands):
            memory_address.append('0'*16)

    while programCounter >= 0 and programCounter < len(commands):
        perform(commands[programCounter])
        track += 1

    memoryDump()