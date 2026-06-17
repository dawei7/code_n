"""Solution for hash_02: Subarray Sum Equals K.

Count the number of contiguous subarrays whose sum equals k.
Trick: the number of subarrays ending at i with sum k equals the
number of earlier prefix sums equal to prefix[i] - k. Hash the
prefix-sum counts. O(n).
Source: https://www.geeksforgeeks.org/number-subarrays-sum-exactly-k/

Inputs passed to solve():
    arr: list of n random integers (can include negatives).
    k: target sum.
    n: length of arr.

Goal:
    the number of contiguous subarrays with sum k.

Samples:
Sample 1 input:  arr = [1, 1, 1], k = 2, n = 3
Sample 1 output: 2 (1+1, 1+1)

Sample 2 input:  arr = [1, 2, 3], k = 3, n = 3
Sample 2 output: 2 (1+2, 3)


"""

def solve(arr, k, n):
    # Write your code here.
    return None
