from solutions import inputFile

def initialize():
    global __movePoints

    global __movesList
    global __outcomes

    global __R
    global __P
    global __S

    VICTORY = 6
    DRAW = 3
    LOSS = 0

    __R = "A"
    __P = "B"
    __S = "C"

    __movePoints = {
        __R: 1,
        __P: 2,
        __S: 3
    }

    __outcomes = {
        __R: lambda m: VICTORY if m == __S else (DRAW if m == __R else LOSS),
        __P: lambda m: VICTORY if m == __R else (DRAW if m == __P else LOSS),
        __S: lambda m: VICTORY if m == __P else (DRAW if m == __S else LOSS)
    }

    with open(inputFile("02"), "r") as f:
        __movesList = list(map(lambda l: l.split(" "), f.read().splitlines()))

def solveFirst():
    encryptedMove = {
        "X": __R,
        "Y": __P,
        "Z": __S
    }

    points = 0
    for round in __movesList:
        moveToPlay = encryptedMove[round[1]]
        roundOutcome = __movePoints[moveToPlay] + __outcomes[moveToPlay](round[0])

        points += roundOutcome

    return points

def solveSecond():
    getVictory = lambda m: __P if m == __R else (__S if m == __P else __R)
    getDraw = lambda m: m
    getLoss = lambda m: __S if m == __R else (__R if m == __P else __P)

    encryptedMove = {
        "X": lambda m: getLoss(m),
        "Y": lambda m: getDraw(m),
        "Z": lambda m: getVictory(m)
    }

    points = 0
    for round in __movesList:
        moveToPlay = encryptedMove[round[1]](round[0])
        roundOutcome = __movePoints[moveToPlay] + __outcomes[moveToPlay](round[0])

        points += roundOutcome

    return points
