"""Optimal solution for sort_11: Cycle Sort.

In-place, write-optimal sort. For each position, count elements
smaller than it to find its final index, then place the value
there. The displaced value starts a new cycle. O(n^2) time,
O(1) extra space, and at most n-1 writes.
"""


def solve(data, n):
    for cycle_start in range(n - 1):
        item = data[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if data[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        # Skip past duplicates of `item` already at `pos`.
        while item == data[pos]:
            pos += 1
        data[pos], item = item, data[pos]
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if data[i] < item:
                    pos += 1
            while item == data[pos]:
                pos += 1
            data[pos], item = item, data[pos]
    return data
