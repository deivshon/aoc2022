import sys

from time import perf_counter_ns

from solutions.list import *

solutionTests = (
    solution01,
    solution02,
    solution03,
    solution04,
    solution05,
    solution06,
    solution07,
    solution08,
    solution09,
    solution10,
    solution11
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

    print(f"{label:>2}: {resFirst:<9} - {resSecond:>9} | {msElapsed:>8.5f}ms")

    return msElapsed

start = 0
end = len(solutionTests)

if len(sys.argv) > 1:
    try:
        start = int(sys.argv[1]) - 1
        end = start + 1
    except:
        print("Error: day argument must be an integer", file = sys.stderr)
        sys.exit(1)

if start >= len(solutionTests) or start < 0:
        print(f"Error: day {start + 1} solution does not exist", file = sys.stderr)
        sys.exit(1)

for i in range(start, end):
    timeSolution(f"{i + 1}", solutionTests[i])

print(f"\nTotal: {solutionsTimeSum:.5f}ms")
