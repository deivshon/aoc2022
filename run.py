import sys

from time import perf_counter_ns

from solutions import day01
from solutions import day02
from solutions import day03

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
    buildSolution(day03.initialize, day03.solveFirst, day03.solveSecond)
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

    print(f"{label}: {resFirst:<8} - {resSecond:>8} | {msElapsed:.5f}ms")

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
