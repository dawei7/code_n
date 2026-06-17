"""Solution for heap_04: Median in a Stream.

Given a stream of integers, return the median after each
insertion. Two heaps: a max-heap of the small half and a
min-heap of the large half; rebalance after every insert.
If the total length is odd, the median is the top of the
larger heap; if even, the average of the two tops.
Requirement: O(n log n) over the whole stream.
Source: https://www.geeksforgeeks.org/median-of-stream-of-running-integers-using-stl/

Inputs passed to solve():
    data: list-like of n random integers (treated as a stream).
    n: length of data.

Goal:
    a list of n medians (one after each insertion).

Samples:
Sample 1 input:  data = [5, 15, 1, 3], n = 4
Sample 1 output: [5, 10.0, 5, 4.0]

Sample 2 input:  data = [2, 4, 6, 8, 10], n = 5
Sample 2 output: [2, 3.0, 4, 5.0, 6]


"""

def solve(data, n):
    # Write your code here.
    return None
