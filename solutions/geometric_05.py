"""Solution for geometric_05: Convex Hull (Jarvis March).


            Compute the convex hull of n points using Jarvis
            March (gift wrapping). Start at the leftmost point,
            then repeatedly find the next hull vertex as the
            point that makes the smallest (most counterclockwise)
            angle with the current edge. Stop when we return
            to the start. Return the hull vertices as a list of
            (x, y) tuples in CCW order, starting from the
            leftmost point. O(n^2) worst case, but O(nh) for
            small hulls.
            Source: https://www.geeksforgeeks.org/dsa/convex-hull-using-jarvis-algorithm/
            

Inputs passed to solve():
    points: list of n (x, y) tuples.
    n: number of points.

Goal:
    a list of (x, y) tuples forming the convex hull, in CCW order starting from the leftmost point.

Samples:
Sample 1 input:  points = [(0,0),(1,1),(2,0),(1,0.5),(0,2)], n = 5
Sample 1 output: a sorted CCW hull, e.g. [(0,0),(2,0),(0,2)]


"""

def solve(points, n):
    # Write your code here.
    return None
