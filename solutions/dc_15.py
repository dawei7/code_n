"""Solution for dc_15: Convex Hull (Divide and Conquer).


            Given n points in the plane, return the vertices of
            the convex hull in counter-clockwise order, as a
            list of (x, y) tuples. The D&C variant sorts the
            points by x, splits at the median, recursively
            computes each half's hull, then merges them with a
            linear-time tangent walk. The verified-oracle uses
            a brute-force O(n^3) gift-wrbing check for small n
            so the test stays accurate.
            Source: https://www.geeksforgeeks.org/dsa/convex-hull-using-divide-and-conquer-algorithm/
            

Inputs passed to solve():
    points: list of n (x, y) integer tuples (small in tests, n <= 10).
    n: number of points.

Goal:
    list of (x, y) tuples on the convex hull in CCW order, starting with the lexicographically smallest point.

Samples:
Sample 1 input:  points = [(0,0), (1,1), (2,0), (1,-1)], n=4
Sample 1 output: [(0,0), (1,1), (2,0), (1,-1)]

Sample 2 input:  points = [(0,3), (1,1), (2,2), (4,4), (0,0), (1,3), (3,1), (3,3)], n=8
Sample 2 output: [(0,0), (1,1), (4,4), (1,3), (0,3)]


"""

def solve(points, n):
    # Write your code here.
    return None
