from solutions import inputFile

def __evaluateTree(grid, line, col):
    height = grid[line][col]
    index = 0

    left = 0
    leftVisible = True
    for index in range(col - 1, -1, -1):
        left += 1
        if grid[line][index] >= height:
            leftVisible = False
            break

    right = 0
    rightVisible = True
    for index in range(col + 1, len(grid[line]), 1):
        right += 1
        if grid[line][index] >= height:
            rightVisible = False
            break

    up = 0
    upVisible = True
    for index in range(line - 1, -1, -1):
        up += 1
        if grid[index][col] >= height:
            upVisible = False
            break

    down = 0
    downVisible = True
    for index in range(line + 1, len(grid), 1):
        down += 1
        if grid[index][col] >= height:
            downVisible = False
            break

    return (
        right * left * up * down,
        rightVisible or leftVisible or upVisible or downVisible
    )

def initialize():
    global __visibleCount
    global __maxScenicScore
    
    __SCENIC_SCORE = 0
    __VISIBLE = 1


    with open(inputFile("08"), "r") as f:
        grid = f.read().splitlines()

    for i in range(0, len(grid)):
        grid[i] = list(map(int, list(grid[i])))

    __visibleCount = 0
    __maxScenicScore = -1

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            treeStats = __evaluateTree(grid, i, j)
            if treeStats[__SCENIC_SCORE] > __maxScenicScore:
                __maxScenicScore = treeStats[__SCENIC_SCORE]
            if treeStats[__VISIBLE]:
                __visibleCount += 1


def solveFirst():
    return __visibleCount

def solveSecond():
    return __maxScenicScore
