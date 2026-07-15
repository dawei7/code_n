from math import gcd


def solve(n: int, a: int, b: int, c: int) -> int:
    def lcm(first: int, second: int) -> int:
        return first // gcd(first, second) * second

    lcm_ab = lcm(a, b)
    lcm_ac = lcm(a, c)
    lcm_bc = lcm(b, c)
    lcm_abc = lcm(lcm_ab, c)

    def count(bound: int) -> int:
        return (
            bound // a
            + bound // b
            + bound // c
            - bound // lcm_ab
            - bound // lcm_ac
            - bound // lcm_bc
            + bound // lcm_abc
        )

    lower = 1
    upper = 2_000_000_000
    while lower < upper:
        middle = lower + (upper - lower) // 2
        if count(middle) >= n:
            upper = middle
        else:
            lower = middle + 1
    return lower
