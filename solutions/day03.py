from solutions import inputFile
from math import floor

def misplacedItem(rucksack):
    for r in rucksack[__COMP1]:
        if r in rucksack[__COMP2]:
            return r

def commonItem(rucksacks):
    items = rucksacks[0][__COMP1] + rucksacks[0][__COMP2]

    for i in items:
        common = True
        for r in rucksacks[1:]:
            if not __inRucksack(i, r):
                common = False
                break

        if common:
            return i

def initialize():
    global __rucksacks
    global __getPriority
    global __inRucksack

    global __COMP1
    global __COMP2
    
    __COMP1 = 0
    __COMP2 = 1

    isLower = lambda c: ord(c) >= 97 and ord(c) <= 122
    __getPriority = lambda c: ord(c) - (96 if isLower(c) else 38)
    __inRucksack = lambda i, r: i in r[__COMP1] or i in r[__COMP2]

    splitRucksackItems = lambda r: [r[0:floor(len(r) / 2)], r[floor(len(r) / 2):len(r)]]

    with open(inputFile("03"), "r") as f:
        __rucksacks = list(map(splitRucksackItems, f.read().splitlines()))

def solveFirst():
    prioritiesSum = 0
    for r in __rucksacks:
        prioritiesSum += __getPriority(misplacedItem(r))

    return prioritiesSum

def solveSecond():
    prioritiesSum = 0
    for i in range(0, len(__rucksacks), 3):
        prioritiesSum += __getPriority(commonItem(__rucksacks[i:i+3]))

    return prioritiesSum
