from solutions import inputFile

def __getDir(path):
    directory = __fs["/"]
    for d in path[1:]:
        directory = directory[__DIR_DATA][d]

    return directory

def __buildDir(path, lsIndex):
    directory = __getDir(path)
    if __DIR_DATA not in directory:
        directory[__DIR_DATA] = {}

    lsIndex += 1

    while lsIndex < len(__terminalOutput) and __terminalOutput[lsIndex][0] != "$":
        name = __terminalOutput[lsIndex][__LS_NAME]
        type = __terminalOutput[lsIndex][__LS_TYPE]

        if __terminalOutput[lsIndex][0] == "dir":
            if name not in directory:
                directory[__DIR_DATA][name] = {}
        else:
            size = type
            directory[__DIR_DATA][name] = int(size)

        lsIndex += 1

def __buildFs():
    currentPath = []

    for i in range(0, len(__terminalOutput)):
        command = __terminalOutput[i][__CMD_INDEX]

        if command == "cd":
            argument = __terminalOutput[i][__ARG_INDEX]
            if argument == "..":
                currentPath.pop()
            else:
                currentPath.append(argument)
        elif command == "ls":
            __buildDir(currentPath, i)

def __appendSizes(current = None):
    if current == None: current = __fs["/"]
    dirData = current[__DIR_DATA]

    size = 0

    for d in dirData.keys():
        if isinstance(dirData[d], int):
            size += dirData[d]
        else:
            __appendSizes(dirData[d])
            size += dirData[d][__DIR_SIZE]

    current[__DIR_SIZE] = size

def initialize():
    global __terminalOutput
    global __fs
    global __currentDir

    global __CMD_INDEX
    global __ARG_INDEX

    global __LS_NAME
    global __LS_TYPE

    global __DIR_SIZE
    global __DIR_DATA

    __CMD_INDEX = 1
    __ARG_INDEX = 2

    __LS_TYPE = 0
    __LS_NAME = 1

    __DIR_SIZE = "size"
    __DIR_DATA = "data"

    __fs = {"/": {__DIR_DATA: {}}}

    with open(inputFile("07"), "r") as f:
        __terminalOutput = list(map(lambda l: l.split(" "), f.read().splitlines()))

    __buildFs()
    __appendSizes()

def solveFirst(current = None):
    if current == None: current = __fs["/"]
    dirData = current[__DIR_DATA]

    res = 0
    if current[__DIR_SIZE] < 100e3:
        res += current[__DIR_SIZE]

    for d in dirData:
        if not isinstance(dirData[d], int):
            res += solveFirst(dirData[d])

    return res

def solveSecond(current = None, free = None, currentMin = None):
    if current == None:
        current = __fs["/"]
        free = 70e6 - __fs["/"][__DIR_SIZE]

    dirData = current[__DIR_DATA]

    if free + current[__DIR_SIZE] > 30e6:
        currentMin = current[__DIR_SIZE]

    for d in dirData:
        if not isinstance(dirData[d], int):
            possibleMin = solveSecond(dirData[d], free, currentMin)
            if possibleMin < currentMin:
                currentMin = possibleMin

    return currentMin
