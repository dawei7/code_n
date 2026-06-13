"""Optimal solution for geometric_06: Rectangle Overlap (Axis-Aligned).

Given two axis-aligned rectangles (each given by its
"""


def solve(l1, r1, l2, r2):
    """Two rectangles do not overlap iff one is entirely left
    of the other, or one is entirely above the other.
    l1 = top-left, r1 = bottom-right (y-axis points up).
    """
    # If rectangle 1 is to the right of rectangle 2, no overlap.
    if l1[0] > r2[0] or l2[0] > r1[0]:
        return False
    # If rectangle 1 is above rectangle 2, no overlap.
    # "Above" means l1.y > r2.y (r1.y is the lower y-bound of rect 1).
    if r1[1] > l2[1] or r2[1] > l1[1]:
        return False
    return True
