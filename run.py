import sys

from time import perf_counter_ns

from solutions import day01
from solutions import day02
from solutions import day03
from solutions import day04
from solutions import day05
from solutions import day06
from solutions import day07
from solutions import day08

INIT = "init"
FIRST = "first"
SECOND = "Second"

buildSolution = lambda init, first, second: {
    INIT: init,
    FIRST: first,
    SECOND: second
}

solutions = (
    buildSolution(day01.initialize, day01.solveFirst, day01.solveSecond),
    buildSolution(day02.initialize, day02.solveFirst, day02.solveSecond),
    buildSolution(day03.initialize, day03.solveFirst, day03.solveSecond),
    buildSolution(day04.initialize, day04.solveFirst, day04.solveSecond),
    buildSolution(day05.initialize, day05.solveFirst, day05.solveSecond),
    buildSolution(day06.initialize, day06.solveFirst, day06.solveSecond),
    buildSolution(day07.initialize, day07.solveFirst, day07.solveSecond),
    buildSolution(day08.initialize, day08.solveFirst, day08.solveSecond)
)

solutionsTimeSum = 0

def timeSolution(label, solution):
    global solutionsTimeSum

    tas = perf_counter_ns()
    solution[INIT]()
    resFirst = solution[FIRST]()
    resSecond = solution[SECOND]()
    tae = perf_counter_ns()

    msElapsed = (tae - tas) / 1e6
    solutionsTimeSum += msElapsed

    print(f"{label}: {resFirst:<9} - {resSecond:>9} | {msElapsed:>8.5f}ms")

    return msElapsed

start = 0
end = len(solutions)

if len(sys.argv) > 1:
    try:
        start = int(sys.argv[1]) - 1
        end = start + 1
    except:
        print("Error: day argument must be an integer", file = sys.stderr)
        sys.exit(1)

if start >= len(solutions) or start < 0:
        print(f"Error: day {start + 1} solution does not exist", file = sys.stderr)
        sys.exit(1)

for i in range(start, end):
    timeSolution(f"{i + 1}", solutions[i])

print(f"\nTotal: {solutionsTimeSum:.5f}ms")
