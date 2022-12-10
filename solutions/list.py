from solutions import day01
from solutions import day02
from solutions import day03
from solutions import day04
from solutions import day05
from solutions import day06
from solutions import day07
from solutions import day08
from solutions import day09

INIT = "init"
FIRST = "first"
SECOND = "second"
RES_FIRST = "resFirst"
RES_SECOND = "resSecond"

__buildTest = lambda init, first, second, resFirst, resSecond: {
    INIT: init,
    FIRST: first,
    SECOND: second,
    RES_FIRST: resFirst,
    RES_SECOND: resSecond
}

solutionTests = (
    __buildTest(
        day01.initialize,
        day01.solveFirst,
        day01.solveSecond,
        71300, 209691),
    __buildTest(
        day02.initialize,
        day02.solveFirst,
        day02.solveSecond,
        13924, 13448),
    __buildTest(
        day03.initialize,
        day03.solveFirst,
        day03.solveSecond,
        7845, 2790),
    __buildTest(
        day04.initialize,
        day04.solveFirst,
        day04.solveSecond,
        459, 779),
    __buildTest(
        day05.initialize,
        day05.solveFirst,
        day05.solveSecond,
        "VCTFTJQCG", "GCFGLDNJZ"),
    __buildTest(
        day06.initialize,
        day06.solveFirst,
        day06.solveSecond,
        1198, 3120),
    __buildTest(
        day07.initialize,
        day07.solveFirst,
        day07.solveSecond,
        1182909, 2832508),
    __buildTest(
        day08.initialize,
        day08.solveFirst,
        day08.solveSecond,
        1560, 252000),
    __buildTest(
        day09.initialize,
        day09.solveFirst,
        day09.solveSecond,
        6212, 2522)
)
