from solutions import inputFile

def getNeighbors(current, grid):
    row = current[0]
    column = current[1]

    neighbors = []
    if row != 0:
        neighbors.append((row - 1, column))
    if column != 0:
        neighbors.append((row, column - 1))
    if row < len(grid) - 1:
        neighbors.append((row + 1, column))
    if column < len(grid[row]) - 1:
        neighbors.append((row, column + 1))

    return neighbors

def dijkstra(grid, start, endCheck, discardCheck):
    unvisited = set()
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            unvisited.add((i, j))

    grid[start[0]][start[1]][__DISTANCE] = 0

    current = start
    currentRow, currentColumn = current[0], current[1]
    while True:
        ownDistance = grid[currentRow][currentColumn][__DISTANCE]
        ownValue = grid[currentRow][currentColumn][__VALUE]

        currentNeighbors = getNeighbors(current, grid)
        for (i, j) in currentNeighbors:
            neighborValue = grid[i][j][__VALUE]
            neighborDistance = grid[i][j][__DISTANCE]
            
            if discardCheck(ownValue, neighborValue):
                continue

            if ownDistance + 1 < neighborDistance:
                grid[i][j][__DISTANCE] = ownDistance + 1
        unvisited.remove(current)

        if len(unvisited) == 0:
            break

        if endCheck(current):
            break

        current = min(unvisited, key = lambda b: grid[b[0]][b[1]][__DISTANCE])

        currentRow, currentColumn = current[0], current[1]

        if grid[currentRow][currentColumn] == __inf:
            break

    return current

def initialize():
    global __VALUE
    global __DISTANCE

    global __START
    global __END

    global __grid

    global __inf

    __inf = float("inf")

    __VALUE = 0
    __DISTANCE = 1

    with open(inputFile("12"), "r") as f:
        __grid = list(map(lambda l: [ord(v) for v in l], f.read().splitlines()))
    
    remaining = 2
    for index, line in enumerate(__grid):
        if ord("S") in line:
            __START = (index, line.index(ord("S")))
            __grid[index][line.index(ord("S"))] = ord("a")
            remaining -= 1
        if ord("E") in line:
            __END = (index, line.index(ord("E")))
            __grid[index][line.index(ord("E"))] = ord("z")
            remaining -= 1

        if remaining == 0: break
    
    for i in range(0, len(__grid)):
        __grid[i] = list(map(lambda v: [v, __inf], __grid[i]))

def solveFirst():
    end = dijkstra(__grid, __START, endCheck = lambda v: v == __END, discardCheck = lambda o, n: n > o + 1)
    return __grid[end[0]][end[1]][__DISTANCE]

def solveSecond():
    for i in range(0, len(__grid)):
        for j in range(0, len(__grid[i])):
            __grid[i][j][__DISTANCE] = __inf

    end = dijkstra(__grid, __END, endCheck = lambda v: __grid[v[0]][v[1]][__VALUE] == ord("a"), discardCheck = lambda o, n: o > n + 1)
    return __grid[end[0]][end[1]][__DISTANCE]
