from bisect import bisect_left, bisect_right


def solve(arr):
    length = len(arr)
    for index in (length // 4, length // 2, 3 * length // 4):
        candidate = arr[index]
        frequency = bisect_right(arr, candidate) - bisect_left(arr, candidate)
        if 4 * frequency > length:
            return candidate
    raise ValueError("the required over-quarter element is missing")
