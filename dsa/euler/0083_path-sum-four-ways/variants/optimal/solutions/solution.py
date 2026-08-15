import heapq
import os


def solve(filepath: str = "") -> int:
    """Find the minimal path sum from top-left (0,0) to bottom-right (79,79) moving UP, DOWN, LEFT, RIGHT using Dijkstra's Algorithm.

    Mathematical Principles Applied:
    1. Shortest Path on a Weighted Grid Graph (Dijkstra's Algorithm):
       The 80x80 matrix represents a grid graph G = (V, E) where |V| = 6400 cells.
       Each directed edge (u, v) has non-negative weight equal to grid[v_r][v_c].
       Since edges can move in all 4 orthogonal directions (up, down, left, right),
       standard dynamic programming fails due to potential cycles.
       Dijkstra's algorithm greedily expands the current minimum-distance node.

    2. Min-Heap Priority Queue Optimization:
       Priority queue pq stores tuples (current_distance, row, col).
       Distance map dist[(r, c)] tracks the shortest path distance found so far.

    Time Complexity: O(V log V) where V = 6,400 cells (executes in ~0.02s).
    Space Complexity: O(V) memory for distance map and priority queue.
    """
    if not filepath:
        # Navigate 4 levels up from solution.py to reach package root (0083_path-sum-four-ways/)
        sol_dir = os.path.dirname(os.path.abspath(__file__))
        pkg_dir = os.path.abspath(os.path.join(sol_dir, "..", "..", ".."))
        filepath = os.path.join(pkg_dir, "matrix.txt")

    # Read matrix text file
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    # Parse 80x80 matrix grid
    grid = [
        [int(x) for x in line.strip().split(",")]
        for line in text.strip().splitlines()
        if line.strip()
    ]
    rows, cols = len(grid), len(grid[0])

    # Distance map initialized with infinity
    dist = {}
    # Priority queue storing tuples: (cumulative_cost, row, col)
    pq = [(grid[0][0], 0, 0)]
    dist[(0, 0)] = grid[0][0]

    # Dijkstra's min-heap expansion loop
    while pq:
        d, r, c = heapq.heappop(pq)

        # Reached target bottom-right node (rows - 1, cols - 1)
        if (r, c) == (rows - 1, cols - 1):
            return d

        # Skip stale priority queue entries
        if d > dist.get((r, c), float("inf")):
            continue

        # Explore 4 orthogonal directions: UP, DOWN, LEFT, RIGHT
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_d = d + grid[nr][nc]
                # Relaxation step: update shortest distance if new path is cheaper
                if new_d < dist.get((nr, nc), float("inf")):
                    dist[(nr, nc)] = new_d
                    heapq.heappush(pq, (new_d, nr, nc))

    return -1


if __name__ == "__main__":
    print(solve())
