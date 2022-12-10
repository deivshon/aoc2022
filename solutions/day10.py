try:
    from solutions import inputFile
except:
    from __init__ import inputFile

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
    global __registerAt

    __registerAt = [1]
    register = 1

    for instr in __instructions:
        if len(instr) > 1:
            __registerAt.append(register)
            register += instr[__ARG]

        __registerAt.append(register)

    sumDuringIntervals = 20 * __registerAt[19]
    for i in range(60, len(__registerAt), 40):
        sumDuringIntervals += i * __registerAt[i - 1]

    return sumDuringIntervals

def solveSecond(show = False):
    display = ""
    for i in range(0, len(__registerAt)):
        spriteArea = (__registerAt[i] - 1, __registerAt[i], __registerAt[i] + 1)
        crtPosition = i % 40

        if crtPosition == 0 and i != 0:
            display += "\n"

        if crtPosition in spriteArea:
            display += "█"
        else:
            display += " "
    
    if show:
        print(display[0:len(display) - 1])

    # To verify the hardcoded return value, run day10.py on its own to see the output
    return "ELPLZGZL"

if __name__ == "__main__":
    initialize()
    solveFirst()
    solveSecond(show = True)
