"""
Description
-----------
Given an array of n integers (with at least one
            element), return the sum of the contiguous subarray
            with the largest sum. The D&C approach: split the
            array at the middle, the answer is the max of (a)
            the best subarray fully in the left half, (b) the
            best fully in the right half, and (c) the best
            subarray that crosses the middle. The crossing sum
            is found in linear time. O(n log n) total.
            Source: https://www.geeksforgeeks.org/dsa/maximum-subarray-sum-using-divide-and-conquer-algorithm/

Examples
--------
Example 1:
Input:  arr = [2, 3, -8, 7, -1, 2, 3], n = 7
Output: 11

Example 2:
Input:  arr = [-2, -4], n = 2
Output: -2

Example 3:
Input:  arr = [5, 4, 1, 7, 8], n = 5
Output: 25

Example 4:
Input:  arr = [2, 3, 4, 5, 7], n = 5
Output: 21
"""

def solve(arr, n):
    # Write your code here.
    return None
