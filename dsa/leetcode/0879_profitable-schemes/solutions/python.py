"""Optimal app-local solution for LeetCode 879."""


MODULUS = 1_000_000_007


def solve(n, minProfit, group, profit):
    schemes = [[0] * (minProfit + 1) for _ in range(n + 1)]
    schemes[0][0] = 1

    for members, gain in zip(group, profit):
        for used in range(n - members, -1, -1):
            for earned in range(minProfit, -1, -1):
                count = schemes[used][earned]
                if count == 0:
                    continue
                next_profit = min(minProfit, earned + gain)
                schemes[used + members][next_profit] = (
                    schemes[used + members][next_profit] + count
                ) % MODULUS

    return sum(row[minProfit] for row in schemes) % MODULUS
