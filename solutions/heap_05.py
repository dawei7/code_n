"""Solution for heap_05: Sliding Window Maximum.

For each window of size k in arr, return the max. Use a
max-heap keyed on (-value, index). Pop from the top
while the index is outside the current window; the heap
top is then the max. O(n log k).
Source: https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-size-k/

Inputs passed to solve():
    arr: list of n integers.
    k: window size (1..4 in the setup).
    n: length of arr.

Goal:
    a list of n - k + 1 maxes (one per window).

Samples:
Sample 1 input:  arr = [1, 3, -1, -3, 5, 3, 6, 7], k = 3, n = 8
Sample 1 output: [3, 3, 5, 5, 6, 7]


"""

def solve(arr, k, n):
    # Write your code here.
    return None
