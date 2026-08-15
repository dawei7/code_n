import os


def contains_origin(ax: int, ay: int, bx: int, by: int, cx: int, cy: int) -> bool:
    """Check if triangle ABC contains the origin O(0,0) via 2D vector cross product orientations.

    Mathematical Principles Applied:
    1. 2D Vector Cross Product Orientations:
       For directed edge AB from A(ax, ay) to B(bx, by), the 2D cross product with origin O(0,0) is:
       cross(A, B) = ax * by - ay * bx.

    2. Point-in-Triangle Orientation Test:
       Origin O(0,0) lies strictly inside triangle ABC iff O lies on the same side of all 3 directed edges
       (AB, BC, CA). That is, the 3 cross products cross(A, B), cross(B, C), cross(C, A) MUST all share the same sign!
       c1 = ax * by - ay * bx
       c2 = bx * cy - by * cx
       c3 = cx * ay - cy * ax
       Condition: (c1 > 0 and c2 > 0 and c3 > 0) or (c1 < 0 and c2 < 0 and c3 < 0).
    """
    c1 = ax * by - ay * bx
    c2 = bx * cy - by * cx
    c3 = cx * ay - cy * ax
    return (c1 > 0 and c2 > 0 and c3 > 0) or (c1 < 0 and c2 < 0 and c3 < 0)


def solve(filepath: str = "") -> int:
    """Find the number of triangles in triangles.txt containing the origin O(0,0).

    Time Complexity: O(N) where N = 1000 lines (executes in ~0.001s).
    Space Complexity: O(N) memory for triangle coordinates.
    """
    if not filepath:
        # Navigate 4 levels up from solution.py to reach package root (0102_triangle-containment/)
        sol_dir = os.path.dirname(os.path.abspath(__file__))
        pkg_dir = os.path.abspath(os.path.join(sol_dir, "..", "..", ".."))
        filepath = os.path.join(pkg_dir, "triangles.txt")

    # Read triangles text file
    with open(filepath, "r", encoding="utf-8") as f:
        lines = [line.strip().split(",") for line in f if line.strip()]

    origin_count = 0
    # Process each triangle line
    for coords in lines:
        ax, ay, bx, by, cx, cy = [int(x) for x in coords]
        if contains_origin(ax, ay, bx, by, cx, cy):
            origin_count += 1

    # Return total count of triangles containing the origin
    return origin_count


if __name__ == "__main__":
    print(solve())
