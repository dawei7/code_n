# Minimum Cost of a Path With Special Roads

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2662 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Graph Theory, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-cost-of-a-path-with-special-roads](https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/).

### Goal
Given a starting point `start` and a target point `target` on an infinite 2D grid, along with a list of `special_roads`, find the minimum cost to travel from `start` to `target`. Movement between any two points `(x1, y1)` and `(x2, y2)` normally incurs a cost equal to their Manhattan distance: `abs(x1 - x2) + abs(y1 - y2)`. However, if a special road `[x1, y1, x2, y2, cost]` exists, you can travel directly from `(x1, y1)` to `(x2, y2)` for the specified `cost`, which might be cheaper or more expensive than the standard Manhattan distance. You can use any combination of normal travel and special roads.

### Function Contract
**Inputs**

- `start`: A list of two integers `[x, y]` representing the starting coordinates.
- `target`: A list of two integers `[x, y]` representing the target coordinates.
- `special_roads`: A list of lists, where each inner list `[x1, y1, x2, y2, cost]` describes a special road from `(x1, y1)` to `(x2, y2)` with a fixed `cost`.

**Return value**

- An integer representing the minimum total cost to reach `target` from `start`.

### Examples
**Example 1**

- Input: `start = [1,1], target = [4,5], special_roads = [[1,1,2,2,1],[2,2,3,3,1],[3,3,4,4,1]]`
- Output: `4`
- Explanation: The Manhattan distance from `(1,1)` to `(4,5)` is `abs(1-4) + abs(1-5) = 3 + 4 = 7`.
  Using special roads: `(1,1) -> (2,2)` costs 1. `(2,2) -> (3,3)` costs 1. `(3,3) -> (4,4)` costs 1.
  From `(4,4)` to `(4,5)` (target) costs `abs(4-4) + abs(4-5) = 0 + 1 = 1`.
  Total cost: `1 + 1 + 1 + 1 = 4`. This is less than 7.

**Example 2**

- Input: `start = [1,1], target = [4,5], special_roads = [[1,1,3,2,4],[3,2,4,3,3]]`
- Output: `7`
- Explanation: The Manhattan distance from `(1,1)` to `(4,5)` is `7`.
  Path 1: `(1,1) -> (3,2)` via special road (cost 4). Then `(3,2) -> (4,5)` via Manhattan distance (`abs(3-4) + abs(2-5) = 1 + 3 = 4`). Total cost: `4 + 4 = 8`.
  Path 2: `(1,1) -> (4,5)` directly via Manhattan distance (cost 7).
  Since 7 is less than 8, the minimum cost is 7.

**Example 3**

- Input: `start = [3,3], target = [5,5], special_roads = [[3,3,5,5,100]]`
- Output: `4`
- Explanation: The Manhattan distance from `(3,3)` to `(5,5)` is `abs(3-5) + abs(3-5) = 2 + 2 = 4`.
  The special road from `(3,3)` to `(5,5)` costs 100. Since 4 is less than 100, the minimum cost is 4.

---

## Solution
### Approach
This problem can be modeled as a shortest path problem on a graph.
1.  **Graph Nodes:** The nodes of our graph are all relevant points: the `start` point, the `target` point, and all `(x1, y1)` and `(x2, y2)` coordinates specified in the `special_roads`. Since coordinates can be large (`10^9`), but the number of special roads is small (up to 200), the total number of distinct points (nodes) in our graph will be relatively small (at most `2 + 2 * 200 = 402` nodes).
2.  **Graph Edges:**
    *   **Manhattan Edges:** Between any two distinct nodes `u` and `v` in our graph, there is an implicit edge with a weight equal to their Manhattan distance `abs(u.x - v.x) + abs(u.y - v.y)`. This represents normal travel.
    *   **Special Road Edges:** For each `special_road = [x1, y1, x2, y2, cost]`, there is a directed edge from `(x1, y1)` to `(x2, y2)` with a weight of `cost`. This cost might be less than, equal to, or greater than the Manhattan distance between these two points.
3.  **Shortest Path Algorithm:** Since all edge weights (both Manhattan distances and special road costs) are non-negative, Dijkstra's algorithm is the optimal choice to find the minimum cost path from `start` to `target`. A min-priority queue (implemented using a heap) is used to efficiently select the unvisited node with the smallest known distance.

### Complexity Analysis
Let `S` be the number of special roads.
The number of distinct points (nodes, `V`) in our graph is at most `2 + 2 * S`. So, `V = O(S)`.
In the worst case, `S = 200`, so `V` is approximately `402`.

-   **Time Complexity**: `O(V^2 log V)` or `O(E log V)` where `E` is the number of edges.
    *   Our graph is dense because we consider Manhattan distance edges between *all pairs* of `V` points. This means `E` is approximately `V^2`.
    *   Therefore, the time complexity for Dijkstra's algorithm becomes `O(V^2 log V)`.
    *   Substituting `V = O(S)`, the complexity is `O(S^2 log S)`.
    *   Given `S <= 200`, `S^2` is `40000`. `log S` (base 2) is approximately `log 200 ≈ 7.6`.
    *   The total operations would be roughly `40000 * 7.6 ≈ 304,000`, which is well within typical time limits for a medium problem.

-   **Space Complexity**: `O(V)`
    *   We store distances for `V` points in a dictionary (`dist`).
    *   The priority queue (`pq`) can store up to `V` elements in the worst case.
    *   The set of `all_points` also stores `V` points.
    *   Substituting `V = O(S)`, the space complexity is `O(S)`.
    *   Given `S <= 200`, this is a very small memory footprint.

### Reference Implementations
<details>
<summary>python</summary>

```python
import heapq

def manhattan_distance(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    """Calculates the Manhattan distance between two points."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve(start: list[int], target: list[int], special_roads: list[list[int]]) -> int:
    """
    Finds the minimum cost to travel from a start point to a target point
    using a combination of normal Manhattan distance travel and special roads.

    Args:
        start: A list [x, y] representing the starting coordinates.
        target: A list [x, y] representing the target coordinates.
        special_roads: A list of lists, where each inner list [x1, y1, x2, y2, cost]
                       describes a special road from (x1, y1) to (x2, y2) with a fixed cost.

    Returns:
        The minimum total cost to reach target from start.
    """
    start_tuple = tuple(start)
    target_tuple = tuple(target)

    # Collect all relevant points that could be intermediate stops or destinations.
    # These include the start, target, and all endpoints of special roads.
    all_points = {start_tuple, target_tuple}
    for sx1, sy1, sx2, sy2, _ in special_roads:
        all_points.add((sx1, sy1))
        all_points.add((sx2, sy2))

    # Initialize distances for all collected points to infinity, except for the start point.
    dist = {point: float('inf') for point in all_points}
    dist[start_tuple] = 0

    # Priority queue stores tuples of (current_cost, point_tuple).
    # It's a min-heap, so the point with the smallest current_cost is always popped first.
    pq = [(0, start_tuple)]

    while pq:
        current_cost, u = heapq.heappop(pq)

        # If we've already found a shorter path to 'u', skip this entry.
        # This can happen because we might add multiple entries for the same node
        # to the priority queue if we find shorter paths to it.
        if current_cost > dist[u]:
            continue

        # If 'u' is the target, we've found the shortest path to it.
        # Since all edge weights are non-negative, this distance is final.
        if u == target_tuple:
            return current_cost

        # Explore paths from 'u':

        # 1. Consider normal Manhattan distance moves to all other relevant points 'v'.
        for v in all_points:
            # A point cannot travel to itself.
            if u == v:
                continue

            cost_uv = manhattan_distance(u, v)

            # If a shorter path to 'v' is found via 'u', update distance and push to PQ.
            if dist[u] + cost_uv < dist[v]:
                dist[v] = dist[u] + cost_uv
                heapq.heappush(pq, (dist[v], v))

        # 2. Consider special roads starting from 'u'.
        for sx1, sy1, sx2, sy2, scost in special_roads:
            # If the special road starts at our current point 'u'.
            if u == (sx1, sy1):
                v = (sx2, sy2)

                # If a shorter path to 'v' is found via this special road from 'u',
                # update distance and push to PQ.
                # 'v' is guaranteed to be in 'all_points' and 'dist' due to initial population.
                if dist[u] + scost < dist[v]:
                    dist[v] = dist[u] + scost
                    heapq.heappush(pq, (dist[v], v))

    # If the target was not reachable (should not happen in this problem as Manhattan distance
    # always provides a path), or if the early return was not triggered,
    # return the final distance to the target.
    return dist[target_tuple]
```
</details>
