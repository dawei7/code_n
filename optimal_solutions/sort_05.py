"""Optimal solution for sort_05: Quick Sort.

Three-way (Dutch National Flag) partition so duplicate keys are
handled in O(n) instead of O(n^2), then drive the recursion
iteratively. Three-way partition is the standard textbook fix
for quicksort's classic "all-equal" infinite loop with Lomuto
partition + the <= comparator, and it also halves the op count
on real data with duplicates.
"""


def solve(data, n):
    def partition_3way(items, low, high):
        # Dutch National Flag partition: items[low..lt-1] are < pivot,
        # items[lt..i-1] are == pivot, items[gt+1..high] are > pivot.
        pivot = items[high]
        lt = low
        i = low
        gt = high
        while i <= gt:
            if items[i] < pivot:
                items.swap(lt, i)
                lt += 1
                i += 1
            elif items[i] > pivot:
                items.swap(i, gt)
                gt -= 1
            else:
                i += 1
        return lt, gt

    stack = [(0, n - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            lt, gt = partition_3way(data, low, high)
            # Both halves may be non-empty.
            if lt - 1 > low:
                stack.append((low, lt - 1))
            if gt + 1 < high:
                stack.append((gt + 1, high))

    return data
