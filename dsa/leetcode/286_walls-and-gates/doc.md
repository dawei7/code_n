# Walls and Gates

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 286 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/walls-and-gates/) |

## Problem Description
### Goal
Given a rectangular grid of rooms, `-1` marks a wall, `0` marks a gate, and `2147483647` marks an empty room. Movement is allowed between horizontally or vertically adjacent cells but cannot pass through walls.

For every empty room that can reach at least one gate, replace its sentinel value with the minimum number of steps to any gate. Modify the grid in place and return nothing. Leave walls and gates unchanged, and leave an unreachable room at `2147483647`. Distances are based on the closest gate independently for each room; diagonal movement and travel outside the grid are forbidden.

### Function Contract
**Inputs**

- `rooms`: a mutable grid where `-1` is a wall, `0` a gate, and `2147483647` an empty room

**Return value**

Returns `None`; the grid is updated in place with nearest-gate distances for every reachable empty room.

### Examples
**Example 1**

- Input: `rooms = [[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]`
- Output: `[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]`

**Example 2**

- Input: `rooms = [[0,INF]]`
- Output: `[[0,1]]`

**Example 3**

- Input: `rooms = [[INF]]`
- Output: `[[INF]]`

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**Treat all gates as one BFS frontier**

Enqueue all gates at distance zero. Expand them together in breadth-first order. When an adjacent cell is still `INF`, assign the current distance plus one and enqueue it.

Every dequeued cell already has its shortest distance to any gate. Unvisited `INF` cells have not yet been reached by a path as short as the current BFS frontier.

**First arrival is the nearest gate distance**

Multi-source BFS is equivalent to adding a virtual source with zero-cost initialization at every gate. Its layers contain cells at increasing distance from the closest source, so the first path reaching a room is shortest. Assigning distance when enqueued prevents a later path of equal or greater length from changing it, while walls are never enqueued.

#### Complexity detail

Each cell is enqueued at most once and checks four neighbors, giving $O(mn)$ time. The queue may contain $O(mn)$ cells.

#### Alternatives and edge cases

- **Run BFS from every empty room:** can take $O((mn)^2)$.
- With no gates, empty rooms stay `INF`; walls can make rooms permanently unreachable.

</details>
