"""Solution for dc_08: Count Inversions.


            Count the number of inversions in an array of n
            integers. An inversion is a pair (i, j) with i < j
            and a[i] > a[j]. The classic O(n log n) approach
            is to count during a merge sort: while merging the
            two sorted halves, every time a right-side element
            is taken first, all remaining left-side elements
            form an inversion with it.
            Source: https://www.geeksforgeeks.org/counting-inversions/
            

Inputs passed to solve():
    arr: list of n integers.
    n: length of arr.

Goal:
    the number of inversions.

Samples:
Sample 1 input:  arr = [2, 4, 1, 3, 5], n = 5
Sample 1 output: 3 (2>1, 4>1, 4>3)

Sample 2 input:  arr = [5, 4, 3, 2, 1], n = 5
Sample 2 output: 10

Sample 3 input:  arr = [1, 2, 3, 4, 5], n = 5
Sample 3 output: 0

"""

def solve(arr, n):
    # Write your code here.
    return None
