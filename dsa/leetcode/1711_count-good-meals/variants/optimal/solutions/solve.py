from collections import defaultdict


def solve(deliciousness: list[int]) -> int:
    modulo = 1_000_000_007
    seen: dict[int, int] = defaultdict(int)
    pairs = 0

    for value in deliciousness:
        power = 1
        while power <= 1 << 21:
            pairs += seen[power - value]
            power <<= 1
        seen[value] += 1

    return pairs % modulo
