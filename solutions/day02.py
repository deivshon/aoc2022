from solutions import inputFile

def __decryptMovesList(movesList):
    for index, move in enumerate(movesList):
        movesList[index][1] = __encryptedMove[move[1]]

def initialize():
    global __movePoints
    global __encryptedMove

    global __decryptMove
    global __getMovePoints
    global __roundPoints

    global __movesList
    global __outcomes

    VICTORY = 6
    DRAW = 3
    LOSS = 0

    __movePoints = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    __encryptedMove = {
        "X": "A",
        "Y": "B",
        "Z": "C"
    }

    __outcomes = {
        "A": lambda m: VICTORY if m == "C" else (DRAW if m == "A" else LOSS),
        "B": lambda m: VICTORY if m == "A" else (DRAW if m == "B" else LOSS),
        "C": lambda m: VICTORY if m == "B" else (DRAW if m == "C" else LOSS)
    }

    __getMovePoints = lambda m: __movePoints[m]
    __roundPoints = lambda m: __getMovePoints(m[1]) + __outcomes[m[1]](m[0])

    with open(inputFile("02"), "r") as f:
        __movesList = list(map(lambda l: l.split(" "), f.read().splitlines()))

    __decryptMovesList(__movesList)

def solveFirst():
    return sum([__roundPoints(r) for r in __movesList])

def solveSecond():
    None
