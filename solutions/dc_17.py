"""Solution for dc_17: Min and Max (D&C tournament).


            Given an array of n integers, return the minimum
            and maximum values using only (3n/2) - 2 comparisons
            in the worst case. The D&C tournament method: for
            n = 1 the min and max are both the element; for n = 2
            they are decided in one comparison; for larger n,
            recursively solve both halves, then take min of the
            mins and max of the maxes (2 more comparisons).
            Source: https://www.geeksforgeeks.org/dsa/maximum-and-minimum-in-an-array/
            

Inputs passed to solve():
    arr: list of n integers (n >= 1).
    n: array length (capped at 32 in tests).

Goal:
    [min(arr), max(arr)] as a 2-element list.

Samples:
Sample 1 input:  arr = [3, 5, 4, 1, 9], n = 5
Sample 1 output: [1, 9]

Sample 2 input:  arr = [22, 14, 8, 17, 35, 3], n = 6
Sample 2 output: [3, 35]

Sample 3 input:  arr = [7], n = 1
Sample 3 output: [7, 7]
Sample 4 input:  arr = [2, 1], n = 2
Sample 4 output: [1, 2]

"""

def solve(arr, n):
    # Write your code here.
    return None
