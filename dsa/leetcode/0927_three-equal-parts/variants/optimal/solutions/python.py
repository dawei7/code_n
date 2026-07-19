"""Optimal app-local solution for LeetCode 927."""


def solve(arr):
    one_count = sum(arr)
    if one_count == 0:
        return [0, 2]
    if one_count % 3:
        return [-1, -1]

    ones_per_part = one_count // 3
    first = second = third = -1
    seen = 0

    for index, bit in enumerate(arr):
        if bit == 0:
            continue
        if seen == 0:
            first = index
        elif seen == ones_per_part:
            second = index
        elif seen == 2 * ones_per_part:
            third = index
        seen += 1

    i, j, k = first, second, third
    while k < len(arr) and arr[i] == arr[j] == arr[k]:
        i += 1
        j += 1
        k += 1

    if k == len(arr):
        return [i - 1, j]
    return [-1, -1]

