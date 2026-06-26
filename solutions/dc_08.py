"""
Description
-----------
Count the number of inversions in an array of n
            integers. An inversion is a pair (i, j) with i < j
            and a[i] > a[j]. The classic O(n log n) approach
            is to count during a merge sort: while merging the
            two sorted halves, every time a right-side element
            is taken first, all remaining left-side elements
            form an inversion with it.
            Source: https://www.geeksforgeeks.org/counting-inversions/

Examples
--------
Example 1:
Input:  arr = [2, 4, 1, 3, 5], n = 5
Output: 3 (2>1, 4>1, 4>3)

Example 2:
Input:  arr = [5, 4, 3, 2, 1], n = 5
Output: 10

Example 3:
Input:  arr = [1, 2, 3, 4, 5], n = 5
Output: 0
"""

def solve(arr, n):
    # Write your code here.
    return None
