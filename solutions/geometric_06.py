"""Solution for geometric_06: Rectangle Overlap (Axis-Aligned).


            Given two axis-aligned rectangles (each given by its
            top-left corner l1, l2 and bottom-right corner r1,
            r2 with l.x <= r.x and l.y >= r.y, i.e., y grows
            upward), determine whether the two rectangles
            overlap (have a positive-area intersection).
            Two rectangles do NOT overlap iff one is entirely
            to the left of the other, or entirely above the
            other. Return True if they overlap, False
            otherwise. O(1).
            Source: https://www.geeksforgeeks.org/dsa/find-two-rectangles-overlap/
            

Inputs passed to solve():
    l1: (x, y) of the top-left corner of rectangle 1.
    r1: (x, y) of the bottom-right corner of rectangle 1.
    l2: (x, y) of the top-left corner of rectangle 2.
    r2: (x, y) of the bottom-right corner of rectangle 2.

Goal:
    True if the rectangles overlap, False otherwise.

Samples:
Sample 1 input:  l1 = (0,10), r1 = (10,0), l2 = (5,5), r2 = (15,0)
Sample 1 output: True (overlap)

Sample 2 input:  l1 = (0,10), r1 = (10,0), l2 = (-10,5), r2 = (-1,0)
Sample 2 output: False (rect2 is left of rect1)


"""

def solve(l1, r1, l2, r2):
    # Write your code here.
    return None
