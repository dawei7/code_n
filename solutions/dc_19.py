"""Solution for dc_19: Maximum Subarray Sum (Divide and Conquer).


            Given an array of n integers (with at least one
            element), return the sum of the contiguous subarray
            with the largest sum. The D&C approach: split the
            array at the middle, the answer is the max of (a)
            the best subarray fully in the left half, (b) the
            best fully in the right half, and (c) the best
            subarray that crosses the middle. The crossing sum
            is found in linear time. O(n log n) total.
            Source: https://www.geeksforgeeks.org/dsa/maximum-subarray-sum-using-divide-and-conquer-algorithm/
            

Inputs passed to solve():
    arr: list of n integers (n >= 1; may include negatives).
    n: array length (capped at 16 in tests).

Goal:
    the maximum subarray sum as an int.

Samples:
Sample 1 input:  arr = [2, 3, -8, 7, -1, 2, 3], n = 7
Sample 1 output: 11

Sample 2 input:  arr = [-2, -4], n = 2
Sample 2 output: -2

Sample 3 input:  arr = [5, 4, 1, 7, 8], n = 5
Sample 3 output: 25
Sample 4 input:  arr = [2, 3, 4, 5, 7], n = 5
Sample 4 output: 21

"""

def solve(arr, n):
    # Write your code here.
    return None
