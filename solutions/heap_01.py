"""Solution for heap_01: Build Max Heap.

Rearrange an array into a 0-indexed binary max-heap: for every
node i, data[i] >= data[2i+1] and data[i] >= data[2i+2].
Bottom-up heapify: sift-down from the last non-leaf to the root.
Mutate the input in place. The output must satisfy the max-heap
property and be a permutation of the input.
Requirement: O(n) time, O(1) extra space.
Source: https://www.geeksforgeeks.org/building-heap-from-array/

Inputs passed to solve():
    data: list-like of n random integers (mutated in place).
    n: length of data.

Goal:
    the same list, now in max-heap order.

Samples:
Sample 1 input:  data = [1, 3, 5, 7, 9, 11], n = 6
Sample 1 output: [11, 9, 5, 7, 3, 1]  (one valid max-heap)

Sample 2 input:  data = [5, 5, 5, 5], n = 4
Sample 2 output: [5, 5, 5, 5]


"""

def solve(data, n):
    # Write your code here.
    return None
