"""
Description
-----------
Given a sorted array of positive integers and a
            value target (also in the limited range), return
            the number of times target appears. Use D&C
            binary search to find the first and last occurrence
            of the target, then frequency = last - first + 1.
            The D&C speedup: instead of O(n) linear scanning,
            each frequency query is O(log n). If the target is
            absent, return 0.
            Source: https://www.geeksforgeeks.org/dsa/find-frequency-of-each-element-in-a-limited-range-array-in-less-than-on-time/

Examples
--------
Example 1:
Input:  arr = [1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10], n = 14, target = 8
Output: 3

Example 2:
Input:  arr = [2, 2, 6, 6, 7, 7, 7, 11], n = 8, target = 6
Output: 2

Example 3:
Input:  arr = [1, 2, 3, 4, 5], n = 5, target = 99
Output: 0
"""

def solve(arr, n, target):
    # Write your code here.
    return None
