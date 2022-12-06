from solutions import inputFile

def __firstDiverseSequence(ls, n):
    for i in range(n, len(ls)):
        if len(set(ls[i - n:i])) == n:
            return i

def initialize():
    global __message

    with open(inputFile("06"), "r") as f:
        __message = f.read().strip()

def solveFirst():
    return __firstDiverseSequence(__message, 4)

def solveSecond():
    return __firstDiverseSequence(__message, 14)
