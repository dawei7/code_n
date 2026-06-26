"""
Description
-----------
Find the index of the target value in a SORTED array.
The array is sorted in ascending order.
Return the index, or -1 if not found.
Requirement: O(log n) - linear search will FAIL!
Source: https://www.geeksforgeeks.org/binary-search/

Examples
--------
Example 1:
Input:  data = [2, 4, 7, 9], target = 7
Output: 2

Example 2:
Input:  data = [1, 5, 8, 12], target = 3
Output: -1

Example 3:
Input:  data = [10, 20, 30], target = 10
Output: 0
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
