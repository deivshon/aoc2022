from solutions import inputFile

def __moveHead(head, direction):
    if direction == "R":
        head[__X] += 1
    elif direction == "L":
        head[__X] -= 1
    elif direction == "U":
        head[__Y] -= 1
    else:
        head[__Y] += 1

def __tailFollow(head, tail):
    xDiff = head[__X] - tail[__X]
    yDiff = head[__Y] - tail[__Y]

    if abs(xDiff) > 1 or abs(yDiff) > 1:
        # Follow head
        xMove = -1 if xDiff < 0 else (0 if xDiff == 0 else 1)
        yMove = -1 if yDiff < 0 else (0 if yDiff == 0 else 1)

        tail[__X] += xMove
        tail[__Y] += yMove

def initialize():
    global __X
    global __Y

    global __firstTailVisited
    global __lastTailVisited

    DIRECTION = 0
    AMOUNT = 1
    
    __X = 0
    __Y = 1

    with open(inputFile("09"), "r") as f:
        moves = map(lambda l: l.split(" "), f.read().splitlines())
    
    moves = list(map(lambda m: [m[DIRECTION], int(m[AMOUNT])], moves))
    
    rope = [[0, 0] for _ in range(0, 10)]

    __firstTailVisited = set()
    __lastTailVisited = set()

    for m in moves:
        for _ in range(0, m[AMOUNT]):
            __moveHead(rope[0], m[DIRECTION])
            for knotIndex in range(1, len(rope)):
                __tailFollow(rope[knotIndex - 1], rope[knotIndex])

            __firstTailVisited.add((rope[1][__X], rope[1][__Y]))
            __lastTailVisited.add((rope[len(rope) - 1][__X], rope[len(rope) - 1][__Y]))

def solveFirst():
    return len(__firstTailVisited)

def solveSecond():
    return len(__lastTailVisited)
