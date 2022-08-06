import sys
import matplotlib.pyplot as plt

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
x=[]
y=[]



#Utility Functions
def memoryDump():
    for i in memory_address:
        print(i)



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




def floattobinary(num,places):
    temp=str(num).split(".")
    w=temp[0]
    d=temp[1]
    w=int(w)
    d=int(d)
    ans=bin(w).lstrip("0b")+"."
    for i in range(places):
        d*=2
        if d>=1:
            d-=1
            ans+="1"
        else:
            ans+="0"
    return ans



# 	whole = int(whole)
# 	dec = int (dec)
# 	res = bin(whole).lstrip("0b") + "."
# 	for x in range(places):
# 		whole, dec = str((decimal_converter(dec)) * 2).split(".")
# 		dec = int(dec)
# 		res += whole
# 	return res


def plot():
    plt.xlabel('Cycle Number')
    plt.ylabel("Memory Address")
    plt.plot(x, y,'o')
    plt.savefig('output.png')

def decimal_converter(num):
	while num > 1:
		num /= 10
	return num


def seperate(num):
    n = num
    count = 0
    while(n > 2):
        count += 1
        n = n/2
    inn = str(int(n))
    linn = len(inn)
    p = len(str(n)) - linn - 1
    return(count, floattobinary(n, p))


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


def binaryToDecimal(binary):
    binary = binary[::-1]
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


def BinaryToFloatingPoint(line):
    a = list(line)
    exp = a[0] + a[1] + a[2]
    mantissa = a[3] + a[4] + a[5] + a[6] + a[7]
    decimalexp = binaryToDecimal(exp)
    mantissaexp = decimalbinaryToDecimal(mantissa)
    ans = (2**(decimalexp))*(1 + mantissaexp)
    return ans


def FloatingPointToBinary(n):
    if (n <= 252 and n >= 0):
        l = list((seperate(n)[1]))
        a = l[2:]      
        la = len(a)
        ans = ""
        while(la < 5):
            a.append("0")
            la += 1
        for i in a:
            ans += str(i)
        temp = (str(decimalToBinaryforexp(seperate(n)[0]))+str(ans))
        return (temp)

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


def addf(line):
    global programCounter
    reg1 = BinaryToFloatingPoint(regs[line[7:10]])
    reg2 = BinaryToFloatingPoint(regs[line[10:13]])
    reg3 = line[13:]
    reg4 = reg1 + reg2

    if reg4 > 256 or reg4 < 0:
        regs["111"] = "0000000000001000"
    else:
        regs["111"] = "0000000000000000"

    regs[reg3] = FloatingPointToBinary(reg4)
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


def subf(line):
    global programCounter
    reg1 = BinaryToFloatingPoint(regs[line[7:10]])
    reg2 = BinaryToFloatingPoint(regs[line[10:13]])
    reg3 = line[13:]
    reg4 = reg1 - reg2

    if reg4 > 256 or reg4 < 0:
        regs["111"] = "0000000000001000"
    else:
        regs["111"] = "0000000000000000"

    regs[reg3] = FloatingPointToBinary(reg4)
    printline()
    programCounter += 1


def movimm(line):
    global programCounter
    reg = line[5:8]
    value = binary2decimal(line[8:])
    regs[reg] = decimal2binary(value)
    printline()
    programCounter += 1


def movf(line):
    global programCounter
    reg = line[5:8]
    value = line[8:]
    regs[reg] = "00000000" + value
    printline()
    programCounter += 1


def movreg(line):
    global programCounter
    regs[line[13:]] = regs[line[10:13]]
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

    if reg4 > 65535 or reg4 < 0:
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

    regs[reg] = decimal2binary(int(regValue) >> int(value))

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def ls(line):
    global programCounter
    reg = line[5:8]
    value = line[8:]
    regValue = binary2decimal(regs[reg])

    regs[reg] = decimal2binary(int(regValue) << int(value))

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def xorop(line):
    global programCounter
    reg1 = decimal2binary(regs[line[7:10]])
    reg2 = decimal2binary(regs[line[10:13]])
    reg3 = line[13:]

    regs[reg3] = decimal2binary(int(reg2) ^ int(reg1))

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def orop(line):
    global programCounter
    reg1 = decimal2binary(regs[line[7:10]])
    reg2 = decimal2binary(regs[line[10:13]])
    reg3 = line[13:]

    regs[reg3] = decimal2binary(int(reg2) | int(reg1))

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1

def andop(line):
    global programCounter
    reg1 = decimal2binary(regs[line[7:10]])
    reg2 = decimal2binary(regs[line[10:13]])
    reg3 = line[13:]

    regs[reg3] = decimal2binary(int(reg2) & int(reg1))

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def notop(line):
    global programCounter
    reg1 = regs[line[10:13]]
    reg2 = line[13:]
    newreg = ""
    for i in reg1:
        if i == '0':
            newreg += "1"
        if i == '1':
            newreg += "0"    
    
    regs[reg2] = newreg
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
        regs["111"] = "0000000000000000"
        printline()
        programCounter = binary2decimal(line[8:])
        return

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def jgt(line):
    global programCounter
    if regs["111"] == "0000000000000010":
        regs["111"] = "0000000000000000"
        printline()
        programCounter = binary2decimal(line[8:])
        return

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1

def getint(string):
    return int(string, 2)



def je(line):
    global programCounter
    if regs["111"] == "0000000000000001":
        regs["111"] = "0000000000000000"
        printline()
        programCounter = binary2decimal(line[8:])
        return

    regs["111"] = "0000000000000000"
    printline()
    programCounter += 1


def hlt(line):
    global programCounter
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
        x.append(track)
        y.append(getint(line[8:]))
    elif opcode == "10101":
        store(line)
        x.append(track)
        y.append(getint(line[8:]))
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
    elif opcode == "00000":
        addf(line)
    elif opcode == "00001":
        subf(line)
    elif opcode == "00010":
        movf(line)


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
            memory_address.append(commands[i])
        if i >= len(commands):
            memory_address.append('0'*16)

    while programCounter >= 0 and programCounter < len(commands):
        x.append(track)
        y.append(programCounter)
        perform(commands[programCounter])
        track += 1

    plot()
    memoryDump()
