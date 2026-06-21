"""Solution for search_02: Binary Search.

Find the index of the target value in a SORTED array.
The array is sorted in ascending order.
Return the index, or -1 if not found.
Requirement: O(log n) - linear search will FAIL!
Source: https://www.geeksforgeeks.org/binary-search/

Inputs passed to solve():
    data: sorted list-like of n random integers.
    target: value to find in data.
    n: length of data.

Goal:
    the index of target in data, or -1 if not found.

Samples:
Sample 1 input:  data = [2, 4, 7, 9], target = 7
Sample 1 output: 2

Sample 2 input:  data = [1, 5, 8, 12], target = 3
Sample 2 output: -1

Sample 3 input:  data = [10, 20, 30], target = 10
Sample 3 output: 0

"""

def solve(data, target, n):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        value = data[mid]
        if value == target:
            return mid
        if value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
