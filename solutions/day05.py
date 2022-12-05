from solutions import inputFile

def __parseStacks(stacksStrings):
    # [0:-1] -> Don't parse stack identifiers
    for line in stacksStrings:
        for i in range(1, len(line), 4):
            if not line[i].isspace():
                stacksIndex = int((i - 1) / 4)
                __stacksFirst[stacksIndex].insert(0, line[i])
                __stacksSecond[stacksIndex].insert(0, line[i])

def __parseMoves(movesStrings):
    for index, line in enumerate(movesStrings):
        splitLine = line.split()
        __moves[index][__AMOUNT] = int(splitLine[1])
        __moves[index][__SOURCE] = int(splitLine[3]) - 1
        __moves[index][__DESTINATION] = int(splitLine[5]) - 1

def __moveCrates(stacks, reverseMultiple):
    verse = -1 if reverseMultiple else 1

    for move in __moves:
        amount = move[__AMOUNT]
        source = move[__SOURCE]
        destination = move[__DESTINATION]

        stacks[destination] += stacks[source][-amount:][::verse]
        stacks[source] = stacks[source][0:-amount]

def __getStackTops(stacks):
    topsString = ""
    for s in stacks:
        topsString += s[-1]

    return topsString

def initialize():
    global __stacksFirst
    global __stacksSecond

    global __moves
    
    global __AMOUNT
    global __SOURCE
    global __DESTINATION

    __AMOUNT = 0
    __SOURCE = 1
    __DESTINATION = 2

    with open(inputFile("05"), "r") as f:
        data = f.read().split("\n\n")

    stacksStrings = data[0].splitlines()[0:-1]
    movesStrings = data[1].splitlines()

    stacksNumber = int((len(stacksStrings[0]) + 1) / 4)
    __stacksFirst = [[] for _ in range(0, stacksNumber)]
    __stacksSecond = [[] for _ in range(0, stacksNumber)]

    __moves = [[-1, -1, -1] for _ in range(0, len(movesStrings))]

    __parseStacks(stacksStrings)
    __parseMoves(movesStrings)

def solveFirst():
    __moveCrates(__stacksFirst, reverseMultiple = True)
    return __getStackTops(__stacksFirst)

def solveSecond():
    __moveCrates(__stacksSecond, reverseMultiple = False)
    return __getStackTops(__stacksSecond)
