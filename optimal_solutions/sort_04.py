"""Optimal solution for sort_04: Merge Sort.

Divide the array in half, sort each half recursively, then merge
the two sorted halves. O(n log n) time, O(n) extra space.
"""


def solve(data, n):
    def merge_sort(items):
        if len(items) <= 1:
            return items
        mid = len(items) // 2
        left = merge_sort(items[:mid])
        right = merge_sort(items[mid:])
        return _merge(left, right)

    def _merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    sorted_items = merge_sort(data)
    # Copy back into the player's TrackedList so the in-place contract
    # is satisfied. Each `data[i] = value` counts as one write.
    for i, value in enumerate(sorted_items):
        data[i] = value
    return data
