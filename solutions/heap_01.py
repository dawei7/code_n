"""
Description
-----------
Rearrange an array into a 0-indexed binary max-heap: for every
node i, data[i] >= data[2i+1] and data[i] >= data[2i+2].
Bottom-up heapify: sift-down from the last non-leaf to the root.
Mutate the input in place. The output must satisfy the max-heap
property and be a permutation of the input.
Requirement: O(n) time, O(1) extra space.
Source: https://www.geeksforgeeks.org/building-heap-from-array/

Examples
--------
Example 1:
Input:  data = [1, 3, 5, 7, 9, 11], n = 6
Output: [11, 9, 5, 7, 3, 1]  (one valid max-heap)

Example 2:
Input:  data = [5, 5, 5, 5], n = 4
Output: [5, 5, 5, 5]
"""

def solve(data, n):
    # Write your code here.
    return None
