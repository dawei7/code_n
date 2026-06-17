"""Solution for approx_06: Bin Packing (First-Fit Decreasing).


            Given a list of item sizes in (0, 1] and unit-
            capacity bins, return the number of bins used by
            First-Fit Decreasing: sort items by size descending,
            then for each item place it in the lowest-index
            existing bin with enough remaining capacity; if
            none, open a new bin. FFD is asymptotically
            11/9-approx (uses at most 11/9 * OPT + 6 bins).
            Source: https://en.wikipedia.org/wiki/First-fit-decreasing_bin_packing
            

Inputs passed to solve():
    sizes: list of n item sizes, each in (0, 1].
    n: number of items.

Goal:
    the number of bins used as a non-negative int.

Samples:
Sample 1 input:  sizes = [0.5, 0.7, 0.3, 0.8, 0.4, 0.6], n = 6
Sample 1 output: 3 (FFD)

Sample 2 input:  sizes = [0.2, 0.5, 0.4, 0.7, 0.1, 0.3, 0.8], n = 7
Sample 2 output: 5 (or any FFD-valid count)


"""

def solve(sizes, n):
    # Write your code here.
    return None
