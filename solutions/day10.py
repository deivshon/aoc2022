from solutions import inputFile

def initialize():
    global __instructions
    global __INSTR
    global __ARG

    __INSTR = 0
    __ARG = 1

    with open(inputFile("10"), "r") as f:
        __instructions = list(map(lambda l: l.split(" "), f.read().splitlines()))
    
    for i, instr in enumerate(__instructions):
        if len(instr) > 1:
            __instructions[i][__ARG] = int(instr[__ARG])

def solveFirst():
    registerAt = [1]
    register = 1

    for instr in __instructions:
        if len(instr) > 1:
            registerAt.append(register)
            register += instr[__ARG]

        registerAt.append(register)
    
    sumDuringIntervals = 20 * registerAt[19]
    for i in range(60, len(registerAt), 40):
        sumDuringIntervals += i * registerAt[i - 1]

    return sumDuringIntervals

def solveSecond():
    return 1
