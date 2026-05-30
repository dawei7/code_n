"""Solution for sort_01: Bubble Sort.

Sort the array using only adjacent comparisons and swaps.
You may only call data.compare(i, i+1) and data.swap(i, i+1).
Requirement: O(n²) - just get it sorted correctly!

Inputs passed to solve():
    data: TrackedList containing n random integers.
    n: number of items in data.

Goal:
    Sort data in ascending order, in place.

Allowed operations for this challenge:
    data.compare(i, i + 1)  # compare adjacent items
    data.swap(i, i + 1)     # swap adjacent items

Return:
    The same TrackedList object after it is sorted.
"""

from code_n.api import TrackedList


def solve(data: TrackedList, n: int) -> TrackedList:
    """Sort the received TrackedList and return it.

    data.compare(i, j) returns:
        -1 if data[i] < data[j]
         0 if data[i] == data[j]
         1 if data[i] > data[j]

    For Bubble Sort, only compare and swap neighboring indices:
        i and i + 1
    """
    raise NotImplementedError("Write your bubble sort here")
