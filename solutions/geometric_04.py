"""
Description
-----------
Given a simple polygon (as a list of (x, y) vertices
            in order) and a query point, return True if the
            point lies inside the polygon and False otherwise.
            Use the ray-casting (even-odd) algorithm: shoot a
            horizontal ray from the point to +infinity and count
            the number of times it crosses a polygon edge. An
            odd count means inside. The point is also
            considered inside if it lies exactly on an edge or
            vertex. O(n) per query.
            Source: https://www.geeksforgeeks.org/dsa/how-to-check-if-a-given-point-lies-inside-a-polygon/

Examples
--------
Example 1:
Input:  polygon = [(0, 0), (10, 0), (10, 10), (0, 10)], point = (5, 5), m = 4
Output: True (inside a square)

Example 2:
Input:  polygon = [(0, 0), (10, 0), (10, 10), (0, 10)], point = (20, 5), m = 4
Output: False (outside)
"""

def solve(polygon, point, m):
    # Write your code here.
    return None
