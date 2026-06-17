"""Solution for heap_02: Kth Largest Element.

Find the kth largest element in an unsorted array. Min-heap of
size k: for each element, push it and pop the smallest if the
heap grows past k. At the end the heap top is the answer.
Requirement: O(n log k) time.
Source: https://www.geeksforgeeks.org/kth-largest-element-in-an-array/

Inputs passed to solve():
    data: list-like of n random integers.
    n: length of data.
    k: which largest (1-indexed: k=1 is the max).

Goal:
    the kth largest element, or -1 if k is out of range.

Samples:
Sample 1 input:  data = [3, 2, 1, 5, 6, 4], n = 6, k = 2
Sample 1 output: 5

Sample 2 input:  data = [7, 4, 6, 3, 9, 8], n = 6, k = 3
Sample 2 output: 7


"""

def solve(data, n, k):
    # Write your code here.
    return None
