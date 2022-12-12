from solutions import day01
from solutions import day02
from solutions import day03
from solutions import day04
from solutions import day05
from solutions import day06
from solutions import day07
from solutions import day08
from solutions import day09
from solutions import day10
from solutions import day11
from solutions import day12

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

solution01 = __buildTest(
    day01.initialize,
    day01.solveFirst,
    day01.solveSecond,
    71300, 209691)
solution02 = __buildTest(
    day02.initialize,
    day02.solveFirst,
    day02.solveSecond,
    13924, 13448)
solution03 = __buildTest(
    day03.initialize,
    day03.solveFirst,
    day03.solveSecond,
    7845, 2790)
solution04 = __buildTest(
    day04.initialize,
    day04.solveFirst,
    day04.solveSecond,
    459, 779)
solution05 = __buildTest(
    day05.initialize,
    day05.solveFirst,
    day05.solveSecond,
    "VCTFTJQCG", "GCFGLDNJZ")
solution06 = __buildTest(
    day06.initialize,
    day06.solveFirst,
    day06.solveSecond,
    1198, 3120)
solution07 = __buildTest(
    day07.initialize,
    day07.solveFirst,
    day07.solveSecond,
    1182909, 2832508)
solution08 = __buildTest(
    day08.initialize,
    day08.solveFirst,
    day08.solveSecond,
    1560, 252000)
solution09 = __buildTest(
    day09.initialize,
    day09.solveFirst,
    day09.solveSecond,
    6212, 2522)
solution10 = __buildTest(
    day10.initialize,
    day10.solveFirst,
    day10.solveSecond,
    14780, "ELPLZGZL")
solution11 = __buildTest(
    day11.initialize,
    day11.solveFirst,
    day11.solveSecond,
    118674, -1)
solution12 = __buildTest(
    day12.initialize,
    day12.solveFirst,
    day12.solveSecond,
    517, 512)
