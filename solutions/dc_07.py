"""Solution for dc_07: Skyline Problem.


            Given n axis-aligned rectangular buildings as
            (left, height, right) triples, return the skyline
            as a list of (x, height) key points. A key point is
            a position where the height changes. Consecutive
            points with the same height are collapsed.
            D&C: recursively get the left and right skylines
            and merge them in O(n). The setup keeps n small
            so an O(n^2) verify is fast.
            Source: https://www.geeksforgeeks.org/divide-and-conquer-set-7-the-skyline-problem/
            

Inputs passed to solve():
    buildings: list of n (left, height, right) triples.
    n: number of buildings (capped at 6).

Goal:
    list of (x, height) key points of the skyline.

Samples:
Sample 1 input:  buildings = [(1, 4, 5), (2, 3, 7), (4, 2, 9)], n = 3
Sample 1 output: [[1, 4], [4, 3], [5, 2], [7, 0], [9, 0]]

Sample 2 input:  buildings = [(0, 3, 5)], n = 1
Sample 2 output: [[0, 3], [5, 0]]


"""

def solve(buildings, n):
    # Write your code here.
    return None
