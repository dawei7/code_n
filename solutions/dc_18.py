"""Solution for dc_18: Frequency in Limited Range (sorted array).


            Given a sorted array of positive integers and a
            value `target` (also in the limited range), return
            the number of times `target` appears. Use D&C
            binary search to find the first and last occurrence
            of the target, then frequency = last - first + 1.
            The D&C speedup: instead of O(n) linear scanning,
            each frequency query is O(log n). If the target is
            absent, return 0.
            Source: https://www.geeksforgeeks.org/dsa/find-frequency-of-each-element-in-a-limited-range-array-in-less-than-on-time/
            

Inputs passed to solve():
    arr: sorted list of n positive integers.
    n: array length (capped at 32 in tests).
    target: the value whose frequency we want.

Goal:
    the count of `target` in `arr` as a non-negative int (0 if absent).

Samples:
Sample 1 input:  arr = [1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10], n = 14, target = 8
Sample 1 output: 3

Sample 2 input:  arr = [2, 2, 6, 6, 7, 7, 7, 11], n = 8, target = 6
Sample 2 output: 2

Sample 3 input:  arr = [1, 2, 3, 4, 5], n = 5, target = 99
Sample 3 output: 0

"""

def solve(arr, n, target):
    # Write your code here.
    return None
