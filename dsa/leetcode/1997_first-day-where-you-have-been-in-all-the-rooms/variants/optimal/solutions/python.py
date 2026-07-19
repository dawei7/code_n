def solve(nextVisit: list[int]) -> int:
    modulo = 1_000_000_007
    first_day = [0] * len(nextVisit)

    for room in range(len(nextVisit) - 1):
        first_day[room + 1] = (
            2 * first_day[room] - first_day[nextVisit[room]] + 2
        ) % modulo

    return first_day[-1]
