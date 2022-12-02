import problems.solution01

from time import perf_counter_ns

def timeSolution(label, initialize, solutionFirst, solutionSecond):
    tas = perf_counter_ns()
    initialize()
    resFirst = solutionFirst()
    resSecond = solutionSecond()
    tae = perf_counter_ns()

    print(f"{label}: {resFirst} - {resSecond} | {(tae - tas) / 1000}ms")

timeSolution("1", problems.solution01.initialize, problems.solution01.solveFirst, problems.solution01.solveSecond)
