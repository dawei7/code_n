def solve(s1: str, s2: str) -> int:
    impossible = 10**9
    no_pair = 0
    cleared = impossible

    for index, target_char in enumerate(s2):
        original = int(s1[index])
        target = int(target_char)
        next_no_pair = impossible
        next_cleared = impossible

        for cost, current in ((no_pair, original), (cleared, 0)):
            if current <= target:
                next_no_pair = min(
                    next_no_pair,
                    cost + target - current,
                )

            if index + 1 < len(s1):
                next_original = int(s1[index + 1])
                pair_cost = (
                    cost
                    + (1 - current)
                    + (1 - next_original)
                    + 1
                    + target
                )
                next_cleared = min(next_cleared, pair_cost)

        no_pair, cleared = next_no_pair, next_cleared

    return -1 if no_pair == impossible else no_pair
