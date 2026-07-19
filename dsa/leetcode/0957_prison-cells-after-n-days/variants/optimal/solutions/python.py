"""Optimal app-local solution for LeetCode 957."""


def solve(cells, n):
    state = tuple(cells)
    seen = {}

    while n > 0:
        if state in seen:
            cycle_length = seen[state] - n
            n %= cycle_length
        seen[state] = n
        if n == 0:
            break
        n -= 1
        state = (0,) + tuple(
            int(state[index - 1] == state[index + 1]) for index in range(1, 7)
        ) + (0,)

    return list(state)
