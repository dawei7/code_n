"""Optimal solution for sort_12: Pancake Sort.

The only allowed operation is ``reverse prefix [0..k]`` for
some k. For each pass, find the maximum in the current
unsorted prefix, flip it to the front, then flip the prefix
to drop the max to the end. O(n^2) flips.
"""


def solve(data, n):
    def flip(end):
        start = 0
        while start < end:
            data[start], data[end] = data[end], data[start]
            start += 1
            end -= 1

    size = n
    while size > 1:
        # Find index of the maximum element in data[0..size-1].
        max_idx = 0
        for i in range(1, size):
            if data[i] > data[max_idx]:
                max_idx = i
        if max_idx != size - 1:
            if max_idx != 0:
                flip(max_idx)
            flip(size - 1)
        size -= 1
    return data
