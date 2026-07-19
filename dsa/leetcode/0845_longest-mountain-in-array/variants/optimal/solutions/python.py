"""Optimal app-local solution for LeetCode 845."""


def solve(arr):
    longest = 0
    up = 0
    down = 0

    for index in range(1, len(arr)):
        rising = arr[index - 1] < arr[index]
        equal = arr[index - 1] == arr[index]

        if equal or (down > 0 and rising):
            up = 0
            down = 0

        if rising:
            up += 1
        elif not equal:
            down += 1

        if up > 0 and down > 0:
            longest = max(longest, up + down + 1)

    return longest

