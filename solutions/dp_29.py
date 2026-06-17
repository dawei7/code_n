"""Solution for dp_29: Longest Increasing Subsequence (Patience Sort).

Length of the longest strictly-increasing subsequence.
Patience sort: maintain a sorted ``tails`` array;
for each value, binary-search the leftmost position in
tails that's >= the value and place it. The final
length of tails is the LIS length. O(n log n).
Source: https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

Inputs passed to solve():
    arr: list of n integers.
    n: length of arr.

Goal:
    the length of the LIS.

Samples:
Sample 1 input:  arr = [10, 22, 9, 33, 21, 50, 41, 60, 80], n = 9
Sample 1 output: 6 (10, 22, 33, 50, 60, 80)

Sample 2 input:  arr = [3, 1, 4, 1, 5, 9, 2, 6], n = 8
Sample 2 output: 4 (1, 4, 5, 9)


"""

def solve(arr, n):
    # Write your code here.
    return None
