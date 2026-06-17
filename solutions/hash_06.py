"""Solution for hash_06: Longest Consecutive Sequence.

Given an unsorted array, return the length of the longest
sequence of consecutive integers. Sort, then walk; O(n
log n). Real O(n) solution uses a set: for each v, if v-1
isn't in the set, walk forward counting.
Source: https://www.geeksforgeeks.org/longest-consecutive-subsequence/

Inputs passed to solve():
    arr: list of n integers (can include duplicates).
    n: length of arr.

Goal:
    the length of the longest consecutive-integer run.

Samples:
Sample 1 input:  arr = [1, 9, 3, 10, 4, 20, 2], n = 7
Sample 1 output: 4 (1,2,3,4)

Sample 2 input:  arr = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42], n = 11
Sample 2 output: 9


"""

def solve(arr, n):
    # Write your code here.
    return None
