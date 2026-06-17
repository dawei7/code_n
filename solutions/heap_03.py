"""Solution for heap_03: Top K Frequent Elements.

Given an array and an integer k, return the k most frequent
elements. Sort the output by descending frequency; ties broken
by descending value. Use a hash map to count, then a max-heap
to extract the top k.
Requirement: O(n log k) time.
Source: https://www.geeksforgeeks.org/find-k-frequent-elements-array/

Inputs passed to solve():
    data: list-like of n integers (small value range to ensure duplicates).
    n: length of data.
    k: how many of the most-frequent to return.

Goal:
    a list of k values, sorted by descending frequency (ties: descending value).

Samples:
Sample 1 input:  data = [1, 1, 1, 2, 2, 3], n = 6, k = 2
Sample 1 output: [1, 2]

Sample 2 input:  data = [4, 4, 4, 5, 5, 6, 7], n = 7, k = 1
Sample 2 output: [4]


"""

def solve(data, n, k):
    # Write your code here.
    return None
