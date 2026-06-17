"""Solution for fenwick_06: Count Inversions (BIT).


            Count the number of inversions in an array: pairs
            (i, j) with i < j and arr[i] > arr[j]. Use a BIT
            on the value coordinate: first compress the values
            to 1..n (preserving rank order, so the result is
            unchanged). Traverse the array from right to left;
            for each arr[i], add prefix(arr[i] - 1) to the
            inversion count (this counts elements smaller than
            arr[i] that are to its right), then add 1 to the
            BIT at index arr[i]. O(n log n) total.
            Source: https://www.geeksforgeeks.org/dsa/inversion-count-in-array-using-bit/
            

Inputs passed to solve():
    arr: list of n integers (may be negative or repeated).
    n: length of arr.

Goal:
    the inversion count as a non-negative int.

Samples:
Sample 1 input:  arr = [8, 4, 2, 1], n = 4
Sample 1 output: 6

Sample 2 input:  arr = [3, 1, 2], n = 3
Sample 2 output: 2

Sample 3 input:  arr = [1, 2, 3, 4], n = 4
Sample 3 output: 0 (sorted)
Sample 4 input:  arr = [4, 3, 2, 1], n = 4
Sample 4 output: 6 (reverse sorted)

"""

def solve(arr, n):
    # Write your code here.
    return None
