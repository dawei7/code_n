"""Optimal app-local solution for LeetCode 1347."""


def solve(s, t):
    balances = [0] * 26
    offset = ord("a")
    for source, target in zip(s, t):
        balances[ord(source) - offset] += 1
        balances[ord(target) - offset] -= 1
    return sum(balance for balance in balances if balance > 0)
