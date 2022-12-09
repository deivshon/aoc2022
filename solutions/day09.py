from solutions import inputFile

def __moveHead(direction):
    if direction == "R":
        __headPos[__X] += 1
    elif direction == "L":
        __headPos[__X] -= 1
    elif direction == "U":
        __headPos[__Y] -= 1
    else:
        __headPos[__Y] += 1

def __tailFollow():
    xDiff = __headPos[__X] - __tailPos[__X]
    yDiff = __headPos[__Y] - __tailPos[__Y]

    if abs(xDiff) <= 1 and abs(yDiff) <= 1:
            # Tail is at least diagonally adjacent to head
            return
    else:
        # Follow head
        xMove = -1 if xDiff < 0 else (0 if xDiff == 0 else 1)
        yMove = -1 if yDiff < 0 else (0 if yDiff == 0 else 1)

        __tailPos[__X] += xMove
        __tailPos[__Y] += yMove

def initialize():
    global __headPos
    global __tailPos
    global __tailVisited

    global __moves

    global __DIRECTION
    global __AMOUNT

    global __X
    global __Y

    __DIRECTION = 0
    __AMOUNT = 1
    
    __X = "x"
    __Y = "y"

    __tailVisited = set()

    with open(inputFile("09"), "r") as f:
        __moves = map(lambda l: l.split(" "), f.read().splitlines())
    
    __moves = list(map(lambda m: [m[__DIRECTION], int(m[__AMOUNT])], __moves))

    __headPos = { __X: 0, __Y: 0 }
    __tailPos = { __X: 0, __Y: 0 }

def solveFirst():
    for m in __moves:
        for _ in range(0, m[__AMOUNT]):
            __moveHead(m[__DIRECTION])
            __tailFollow()
            __tailVisited.add((__tailPos[__X], __tailPos[__Y]))

    return len(__tailVisited)

def solveSecond():
    return 1
