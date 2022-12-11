from solutions import inputFile
from math import floor

class Monkey:
    def __init__(self, items, operation, divisor, monkeyTrue, monkeyFalse):
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.monkeyTrue = monkeyTrue
        self.monkeyFalse = monkeyFalse

        self.inspected = 0

def buildMonkey(monkeyParagraph):
    items = list(map(int, monkeyParagraph[1].split(":")[1].split(",")))
    
    add = lambda b: lambda a: a + b
    mul = lambda b: lambda a: a * b

    operation = monkeyParagraph[2].split(":")[1].split(" ")
    secondOperand = operation[5]
    operationFunction = operation[4]

    integerOperand = False
    if secondOperand != "old":
        integerOperand = True
        secondOperand = int(secondOperand)
    
    if operationFunction == "+":
        operation = add(secondOperand) if integerOperand else lambda o: o + o
    elif operationFunction == "*":
        operation = mul(secondOperand) if integerOperand else lambda o: o * o

    divisor = int(monkeyParagraph[3].split(":")[1].split(" ")[-1])
    monkeyTrue = int(monkeyParagraph[4].split(":")[1].split(" ")[-1])
    monkeyFalse = int(monkeyParagraph[5].split(":")[1].split(" ")[-1])

    return Monkey(items, operation, divisor, monkeyTrue, monkeyFalse)

def playRound(monkeys):
    for m in monkeys:
        for _ in range(0, len(m.items)):
            # The current item is always thrown, so the
            # item to analyze is always at index 0
            m.items[0] = m.operation(m.items[0])
            m.items[0] = floor(m.items[0] / 3)
            m.inspected += 1

            destinationMonkey = m.monkeyTrue if m.items[0] % m.divisor == 0 else m.monkeyFalse

            monkeys[destinationMonkey].items.append(m.items.pop(0))


def initialize():
    global __monkeys

    __monkeys = []

    with open(inputFile("11"), "r") as f:
        monkeyData = f.read().split("\n\n")
    
    for paragraph in monkeyData:
        __monkeys.append(buildMonkey(paragraph.splitlines()))

def solveFirst():
    for _ in range(0, 20):
        playRound(__monkeys)

    # Get two most active monkeys without changing the monkeys list
    indexMax = max(enumerate(__monkeys), key = lambda m: m[1].inspected)[0]
    maxMonkey = __monkeys.pop(indexMax)

    indexSecondMax = max(enumerate(__monkeys), key = lambda m: m[1].inspected)[0]

    __monkeys.insert(indexMax, maxMonkey)

    return __monkeys[indexMax].inspected * __monkeys[indexSecondMax].inspected

def solveSecond():
    return -1
