# The Maze III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 499 |
| Difficulty | Hard |
| Topics | Array, String, Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path |
| Official Link | [LeetCode](https://leetcode.com/problems/the-maze-iii/) |

## Problem Description
### Goal
Given a maze, a ball position, and a hole, choose rolling directions `u`, `d`, `l`, and `r`. After a direction is chosen, the ball continues through open cells until a wall stops it, except that reaching the hole ends the route immediately even when the ball could otherwise roll farther.

Return a direction string for a route that makes the ball fall into the hole using the minimum traveled distance, where distance counts open cells crossed. If several routes have the same shortest distance, return the lexicographically smallest direction string; if the hole is unreachable, return `"impossible"`. Direction changes are allowed only after the ball stops.

### Function Contract
**Inputs**

- `maze`: a rectangular binary matrix where `0` is open and `1` is a wall
- `ball`: the starting open cell as `[row, column]`
- `hole`: the target open cell where rolling stops immediately

**Return value**

- The lexicographically smallest shortest path using `d`, `l`, `r`, and `u`, or `"impossible"`

### Examples
**Example 1**

- Input: `maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], ball = [4,3], hole = [0,1]`
- Output: `"lul"`

**Example 2**

- Input: `maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], ball = [4,3], hole = [3,0]`
- Output: `"impossible"`

**Example 3**

- Input: `maze = [[0,0,0],[0,0,0],[0,0,0]], ball = [0,0], hole = [2,2]`
- Output: `"dr"`

### Required Complexity

- **Time:** $O(rows \cdot cols \log(rows \cdot cols))$
- **Space:** $O(rows \cdot cols)$

<details>
<summary>Approach</summary>

#### General

**Precompute where wall-bounded rolls stop**

Scan every row and column into maximal open segments. For each cell, record its left, right, top, and bottom segment endpoints. This replaces repeated corridor walks with constant-time transitions.

**Let the hole interrupt an endpoint transition**

For a proposed direction, first read the wall-bounded endpoint. If the hole lies on that same row or column between the current cell and the endpoint, replace the endpoint with the hole because the ball falls immediately. The edge weight is the coordinate distance traveled.

**Run Dijkstra with path strings in the priority key**

Heap entries are `(distance, path, row, column)`. The heap therefore chooses shorter distance first and, for equal distance, lexicographically smaller path. Store the best `(distance, path)` pair for each stopping cell and relax an edge only when that tuple improves.

**Why returning the first popped hole is valid**

All roll lengths are nonnegative, so Dijkstra finalizes states in nondecreasing distance. The path string is the secondary key for equal distances, and stale entries are discarded against the best-state map. Consequently the first current entry for the hole has minimum distance and the smallest path among all such routes.

#### Complexity detail

Endpoint preprocessing takes $O(rows \cdot cols)$ time. The stopping-cell graph has at most `rows * cols` vertices and four edges per vertex; heap operations give $O(rows \cdot cols \log(rows \cdot cols))$ time. Endpoint tables, best states, and the heap use $O(rows \cdot cols)$ structural space, excluding stored path-string characters.

#### Alternatives and edge cases

- **Roll step by step during Dijkstra:** is correct but may rescan the same corridors from many states.
- **Linear frontier selection:** preserves Dijkstra's result but can take quadratic time in reachable stopping states.
- **Bellman-Ford relaxation:** is correct for the roll graph but repeatedly scans every edge and is unnecessarily expensive for nonnegative weights.
- **Breadth-first search:** minimizes direction changes, not traveled distance, so it solves the wrong objective.
- **Hole before the wall:** stop at the hole even though the ordinary roll endpoint is farther away.
- **Equal distances:** compare the complete direction strings lexicographically.
- **Ball already at hole:** return the empty path.
- **Unreachable hole:** return `"impossible"` after the heap empties.
- **Direction ordering:** the heap path key determines ties; neighbor enumeration alone is insufficient.

</details>
