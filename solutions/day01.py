from solutions import inputFile

def __getCaloriesTop(n):
    return sum([sum(e) for e in __sortedElvesList[0:n]])

def __getElvesLists(data):
    return list(map(lambda e: [int(v) for v in e], map(lambda s: s.splitlines(), data.split("\n\n"))))

def initialize():
    global __sortedElvesList
    with open(inputFile("01"), "r") as f:
        __sortedElvesList = sorted(__getElvesLists(f.read()), key = lambda e: sum(e), reverse = True)

def solveFirst():
    return __getCaloriesTop(1)

def solveSecond():
    return __getCaloriesTop(3)
