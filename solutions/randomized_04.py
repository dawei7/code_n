"""Solution for randomized_04: Randomized Binary Search.


            Given a sorted list of n distinct integers and a
            query value, return the index of the query in the
            list (0-indexed) or -1 if not found. Instead of
            the standard deterministic binary search that
            always picks the middle, the randomized variant
            picks a uniformly random index in the current
            search range [lo, hi] as the pivot each step.
            Expected O(log n) time; O(1) extra space.
            Source: https://www.geeksforgeeks.org/dsa/randomized-binary-search-algorithm/
            

Inputs passed to solve():
    arr: list of n distinct integers, sorted ascending.
    n: length of arr.
    target: value to search for.

Goal:
    the index of target in arr (0-indexed), or -1 if not present.

Samples:
Sample 1 input:  arr = [1, 2, 3, 4, 5, 6, 7, 8], n = 8, target = 5
Sample 1 output: 4

Sample 2 input:  arr = [1, 3, 5, 7, 9], n = 5, target = 100
Sample 2 output: -1


"""

def solve(arr, n, target):
    # Write your code here.
    return None
