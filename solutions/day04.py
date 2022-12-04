from solutions import inputFile

def __contained(r1, r2):
    return r2[0] >= r1[0] and r2[1] <= r1[1]

def __overlap(r1, r2):
    if r2[1] > r1[1]:
        return r2[0] <= r1[1] 
    else:
        return r2[1] >= r1[0] 

def initialize():
    global __assignments

    with open(inputFile("04"), "r") as f:
        __assignments = list(map(lambda r: r.split(","), f.read().splitlines()))
    
    for i, a in enumerate(__assignments):
        # Parse range
        __assignments[i][0] = a[0].split("-")
        __assignments[i][1] = a[1].split("-")

        # Convert start-end pairs to int
        __assignments[i][0][0] = int(a[0][0])
        __assignments[i][0][1] = int(a[0][1])

        __assignments[i][1][0] = int(a[1][0])
        __assignments[i][1][1] = int(a[1][1])

def solveFirst():
    contained = 0
    for a in __assignments:
        if __contained(a[0], a[1]) or __contained(a[1], a[0]):
            contained += 1

    return contained

def solveSecond():
    overlap = 0
    for a in __assignments:
        if __overlap(a[0], a[1]):
            overlap += 1

    return overlap
