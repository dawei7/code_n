"""Solution for dc_05: Closest Pair of Points.


            Given n points in the plane, return the smallest
            Euclidean distance between any two of them. The
            classic O(n log n) plane-sweep algorithm: split
            by the median x, recurse on each half, then check
            the strip of points within `d` of the cut. Brute
            force O(n^2) verify is fine for the small n we use.
            Source: https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer/
            

Inputs passed to solve():
    points: list of n (x, y) integer tuples.
    n: number of points (capped at 8 in the setup).

Goal:
    the minimum pairwise Euclidean distance (float).

Samples:
Sample 1 input:  points = [(0, 0), (5, 0), (3, 4)], n = 3
Sample 1 output: 3.0 (between (0,0) and (3,4))

Sample 2 input:  points = [(0, 0), (1, 1), (2, 2), (3, 3)], n = 4
Sample 2 output: 1.4142135... (sqrt 2)


"""

def solve(points, n):
    # Write your code here.
    return None
