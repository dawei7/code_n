"""Optimal app-local solution for LeetCode 997."""


def solve(n, trust):
    score = [0] * (n + 1)
    for trusting, trusted in trust:
        score[trusting] -= 1
        score[trusted] += 1

    for person in range(1, n + 1):
        if score[person] == n - 1:
            return person
    return -1
