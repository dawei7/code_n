"""Optimal app-local solution for LeetCode 873."""


def solve(arr):
    index_by_value = {value: index for index, value in enumerate(arr)}
    lengths = {}
    best = 0

    for right in range(len(arr)):
        for middle in range(right):
            previous_value = arr[right] - arr[middle]
            if previous_value >= arr[middle]:
                continue
            left = index_by_value.get(previous_value)
            if left is None:
                continue

            length = lengths.get((left, middle), 2) + 1
            lengths[(middle, right)] = length
            best = max(best, length)

    return best
