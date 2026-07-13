# Swim in Rising Water

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 778 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/swim-in-rising-water/) |

## Problem Description

### Goal

An $n \times n$ grid gives the elevation of every square, and rain raises the water level to `t` at time `t`. A square can be occupied once its elevation is at most the current water level, and movement is allowed only between horizontally or vertically adjacent swimmable squares.

Starting at `(0, 0)`, return the minimum time at which $(n - 1, n - 1)$ can be reached. Equivalently, minimize the highest elevation encountered along a valid path; path length itself does not affect the time.

### Function Contract

**Inputs**

- `grid`: a nonempty $n \times n$ matrix whose distinct elevations are the integers from `0` through $n^{2} - 1$.

**Return value**

- The minimum possible value of the highest elevation encountered on a path from `(0, 0)` to $(n - 1, n - 1)$.

### Examples

**Example 1**

- Input: `grid = [[0,2],[1,3]]`
- Output: `3`
- Explanation: The destination itself has elevation `3`, so no earlier arrival is possible.

**Example 2**

- Input: `grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]`
- Output: `16`
- Explanation: The low-elevation route winds around the grid and reaches the destination once elevation `16` is available.

**Example 3**

- Input: `grid = [[0]]`
- Output: `0`
- Explanation: The start is already the destination.

### Required Complexity

- **Time:** $O(n^2 \log n)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**View a path by its highest cell**

For any route, the first usable time is the maximum elevation on that route. The task is therefore a minimax path problem: minimize that maximum rather than a sum of edge weights.

**Expand the lowest frontier cell**

Begin with the top-left cell in a min-heap. Repeatedly remove the frontier cell with the smallest elevation, update the largest elevation removed so far, and add each unvisited neighbor. This is the same cut choice used by Prim's algorithm: among every cell adjacent to the currently reachable region, the lowest one is the earliest cell through which that region can expand.

**Why reaching the destination is final**

When a cell of elevation `e` is removed, all lower frontier choices have already been processed. The running maximum is exactly the lowest water level that can connect the start to the removed region. If the destination is removed at level `t`, the chosen expansions provide a path whose elevations are at most `t`. Any hypothetical path requiring a smaller level would have crossed the frontier through a lower cell and would have been explored earlier, so no smaller answer exists.

#### Complexity detail

There are $n^{2}$ cells. Each cell enters and leaves the heap at most once, and a heap operation costs $O(\log(n^2)) = O(\log n)$, for $O(n^2 \log n)$ time. The heap and visited set can each hold $O(n^2)$ cells.

#### Alternatives and edge cases

- **Binary search plus reachability:** Test whether a DFS or BFS can reach the destination below a chosen water level; this also takes $O(n^2 \log n)$ time over the bounded elevation range.
- **Union-find activation:** Activate cells in increasing elevation order and union active neighbors; the bounded distinct elevations allow $O(n^2 \alpha(n^2))$ time and $O(n^2)$ space.
- **Increment every water level:** Repeating a full reachability search for every possible elevation is correct but can take $O(n^4)$ time.
- **Single cell:** Return its elevation immediately because the start and destination coincide.
- **High endpoint:** The answer is always at least the larger elevation of the two endpoints.
- **Visited timing:** Mark a cell when it enters the heap so it cannot be enqueued repeatedly from different neighbors.
- **Four-directional movement:** Diagonal adjacency must not be used.

</details>
