import solutions.day01

from time import perf_counter_ns

solutionTimeSum = 0

def timeSolution(label, initialize, solutionFirst, solutionSecond):
    global solutionTimeSum

    tas = perf_counter_ns()
    initialize()
    resFirst = solutionFirst()
    resSecond = solutionSecond()
    tae = perf_counter_ns()

    msElapsed = (tae - tas) / 1e6
    solutionTimeSum += msElapsed

    print(f"{label}: {resFirst} - {resSecond} | {msElapsed}ms")

    return msElapsed


timeSolution("1", solutions.day01.initialize, solutions.day01.solveFirst, solutions.day01.solveSecond)

print(f"\nTotal: {solutionTimeSum}ms")
