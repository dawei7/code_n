"""
Description
-----------
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

Examples
--------
Example 1:
Input:  arr = [8, 4, 2, 1], n = 4
Output: 6

Example 2:
Input:  arr = [3, 1, 2], n = 3
Output: 2

Example 3:
Input:  arr = [1, 2, 3, 4], n = 4
Output: 0 (sorted)

Example 4:
Input:  arr = [4, 3, 2, 1], n = 4
Output: 6 (reverse sorted)
"""

def solve(arr, n):
    # Write your code here.
    return None
