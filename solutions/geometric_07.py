"""Solution for geometric_07: Max Points on Same Line.


            Given n points in the plane, find the maximum
            number of points that lie on the same straight line.
            For each pivot point, compute the slope to every
            other point (as a normalized (dy, dx) pair to avoid
            floating-point precision issues). Group points by
            slope and track the max group size. Handle vertical
            lines and duplicate points separately. O(n^2 log n)
            with the hash map, O(n^2) without.
            Source: https://www.geeksforgeeks.org/dsa/count-maximum-points-on-same-line/
            

Inputs passed to solve():
    points: list of n (x, y) integer tuples.
    n: number of points.

Goal:
    the maximum number of points on the same line, as an int.

Samples:
Sample 1 input:  points = [(-1,1),(0,0),(1,1),(2,2),(3,3),(3,4)], n = 6
Sample 1 output: 4 (the line y=x has 4 points)

Sample 2 input:  points = [(0,0),(1,0),(0,1),(1,1)], n = 4
Sample 2 output: 2 (no three collinear)


"""

def solve(points, n):
    # Write your code here.
    return None
