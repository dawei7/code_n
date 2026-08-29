from math import sqrt


def solve(target_left: int = 3, target_below: int = 3) -> int:
    """Find the largest n for which the index of S_n is (target_left, target_below).

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Hyperbola Square Placement Geometry:
       For region 1 <= x and 0 <= y <= 1/x, a square with bottom-left corner at (x_0, y_0)
       and side length s touches the curve (x_0 + s)(y_0 + s) = 1.
       The exact side length is the positive root of s^2 + (x_0 + y_0)s + (x_0 y_0 - 1) = 0:
           s = (-(x_0 + y_0) + sqrt((x_0 - y_0)^2 + 4)) / 2.

    2. Binary Quadtree Partition:
       Placing square S_n creates two subregions:
       - Right subregion: (x_0 + s, y_0) with index (left + 1, below).
       - Top subregion:   (x_0, y_0 + s) with index (left, below + 1).

    3. Minimal Target Threshold & Tree Counting:
       Squares are placed in strictly descending order of side length.
       - The smallest square with index (3, 3) is found by exploring all C(6, 3) = 20
         combinatorial paths of 3 right and 3 top moves.
       - Its side length s_min establishes a strict cutoff: every square placed at or before
         the final (3, 3) square must have s >= s_min.
       - Counting all nodes in the binary partition tree with s >= s_min gives the exact
         1-based placement index of the final (3, 3) square.

    Complexity:
    -----------
    - Time Complexity: O(ans) stack traversal (~0.5 seconds).
    - Space Complexity: O(depth) stack memory (< 1 MB).
    """

    def get_side(x: float, y: float) -> float:
        disc = (x - y) * (x - y) + 4.0
        return (-(x + y) + sqrt(disc)) / 2.0

    # 1. Find the side length of the smallest (target_left, target_below) square
    target_sides = []

    def find_target_sides(x: float, y: float, l: int, b: int) -> None:
        s = get_side(x, y)
        if l == target_left and b == target_below:
            target_sides.append(s)
            return
        if l < target_left:
            find_target_sides(x + s, y, l + 1, b)
        if b < target_below:
            find_target_sides(x, y + s, l, b + 1)

    find_target_sides(1.0, 0.0, 0, 0)
    s_min_target = min(target_sides)

    # 2. Count all squares in the infinite binary tree with side >= s_min_target
    stack = [(1.0, 0.0)]
    count = 0

    while stack:
        x, y = stack.pop()
        s = get_side(x, y)
        if s >= s_min_target:
            count += 1
            stack.append((x + s, y))
            stack.append((x, y + s))

    return count


if __name__ == "__main__":
    print(solve())
