"""
Description
-----------
Given an array arr[] of n book page counts and m
            students, allocate contiguous page blocks to each
            student so that the maximum pages any one student
            gets is minimised. Binary search on the answer:
            for a candidate max mx, greedily assign pages to
            students, count how many are needed, and check if
            m is achievable. The minimum feasible mx is the
            answer.
            Source: https://www.geeksforgeeks.org/dsa/allocate-minimum-number-pages/

Examples
--------
Example 1:
Input:  arr = [10, 20, 30, 40], n = 4, m = 2
Output: 60

Example 2:
Input:  arr = [10, 20, 30], n = 3, m = 1
Output: 60

Example 3:
Input:  arr = [10, 20, 30], n = 3, m = 3
Output: 30
"""

def solve(arr, n, m):
    # Write your code here.
    return None
