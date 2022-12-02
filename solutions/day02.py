from solutions import inputFile

def __decryptMovesList(movesList):
    for index, move in enumerate(movesList):
        movesList[index][1] = __encryptedMove[move[1]]

def initialize():
    global __movePoints
    global __encryptedMove

    global __decryptMove

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

    __outcomes = {
        "A": lambda m: VICTORY if m == "C" else (DRAW if m == "A" else LOSS),
        "B": lambda m: VICTORY if m == "A" else (DRAW if m == "B" else LOSS),
        "C": lambda m: VICTORY if m == "B" else (DRAW if m == "C" else LOSS)
    }

    with open(inputFile("02"), "r") as f:
        __movesList = list(map(lambda l: l.split(" "), f.read().splitlines()))

def solveFirst():
    encryptedMove = {
        "X": "A",
        "Y": "B",
        "Z": "C"
    }

    points = 0
    for round in __movesList:
        moveToPlay = encryptedMove[round[1]]
        roundOutcome = __movePoints[moveToPlay] + __outcomes[moveToPlay](round[0])

        points += roundOutcome

    return points

def solveSecond():
    None
