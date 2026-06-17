"""Solution for dc_03: Kth Smallest (Quickselect).

Return the kth smallest element in an unsorted array (k is
1-indexed). Quickselect: partition like quicksort, then
recurse only into the half that contains the answer. O(n)
average, O(n^2) worst case on pathological data; the setup
shuffles the input to keep the worst case rare.
Source: https://www.geeksforgeeks.org/quickselect-algorithm/

Inputs passed to solve():
    arr: list of n random integers (shuffled).
    k: 1-indexed rank to return.
    n: length of arr.

Goal:
    the kth smallest element, or -1 if k is out of range.

Samples:
Sample 1 input:  arr = [7, 10, 4, 3, 20, 15], k = 3, n = 6
Sample 1 output: 7

Sample 2 input:  arr = [5, 5, 5], k = 1, n = 3
Sample 2 output: 5


"""

def solve(arr, k, n):
    # Write your code here.
    return None
