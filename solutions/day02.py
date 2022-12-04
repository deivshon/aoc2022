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

    __movePoints = { __R: 1, __P: 2, __S: 3 }

    __outcomes = {
        __R: { __S: VICTORY, __R: DRAW, __P: LOSS },
        __P: { __R: VICTORY, __P: DRAW, __S: LOSS },
        __S: { __P: VICTORY, __S: DRAW, __R: LOSS }
    }

    with open(inputFile("02"), "r") as f:
        __movesList = list(map(lambda l: l.split(" "), f.read().splitlines()))

def solveFirst():
    encryptedMove = { "X": __R, "Y": __P, "Z": __S }

    points = 0
    for round in __movesList:
        moveToPlay = encryptedMove[round[1]]
        roundOutcome = __movePoints[moveToPlay] + __outcomes[moveToPlay][round[0]]

        points += roundOutcome

    return points

def solveSecond():
    encryptedMove = {
        "X": { __R: __S, __P: __R, __S: __P },
        "Y": { __R: __R, __P: __P, __S: __S },
        "Z": { __R: __P, __P: __S, __S: __R }
    }

    points = 0
    for round in __movesList:
        moveToPlay = encryptedMove[round[1]][round[0]]
        roundOutcome = __movePoints[moveToPlay] + __outcomes[moveToPlay][round[0]]

        points += roundOutcome

    return points
