import solutions.day01
import solutions.day02

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

    print(f"{label}: {resFirst:<8} - {resSecond:>8} | {msElapsed:.5f}ms")

    return msElapsed


timeSolution("1", solutions.day01.initialize, solutions.day01.solveFirst, solutions.day01.solveSecond)
timeSolution("2", solutions.day02.initialize, solutions.day02.solveFirst, solutions.day02.solveSecond)

print(f"\nTotal: {solutionTimeSum:.5f}ms")
