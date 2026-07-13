# 01 Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 542 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/01-matrix/) |

## Problem Description
### Goal
Given a nonempty binary matrix containing at least one `0`, compute a distance for every cell. Movement is allowed one step at a time between horizontally or vertically adjacent cells, and each step has distance one.

Return a matrix of the same dimensions where entry `(r, c)` is the minimum number of steps from the input cell `(r, c)` to any cell containing zero. Every zero has distance zero, diagonal movement is not allowed, and different cells may use different nearest zeroes. Preserve the input shape and return distances rather than paths or nearest-zero coordinates.

### Function Contract
**Inputs**

- `mat`: a nonempty rectangular matrix of zeros and ones containing at least one zero

**Return value**

- A matrix of the same dimensions where each entry is the minimum number of horizontal or vertical steps to any zero

### Examples
**Example 1**

- Input: `mat = [[0,0,0],[0,1,0],[0,0,0]]`
- Output: `[[0,0,0],[0,1,0],[0,0,0]]`

**Example 2**

- Input: `mat = [[0,0,0],[0,1,0],[1,1,1]]`
- Output: `[[0,0,0],[0,1,0],[1,2,1]]`

**Example 3**

- Input: `mat = [[1,1,0,1]]`
- Output: `[[2,1,0,1]]`

### Required Complexity

- **Time:** $O(rows \cdot cols)$
- **Space:** $O(rows \cdot cols)$

<details>
<summary>Approach</summary>

#### General

**Reverse the direction of the searches**

Starting a search from every one repeats large portions of the grid. Instead, treat all zero cells as simultaneous sources. Their own answer is zero, and every other cell awaits the first zero-origin wave that reaches it.

**Initialize one shared breadth-first queue**

Create a distance matrix containing zero for source cells and `-1` for unvisited ones. Enqueue every zero before traversal begins. This represents BFS level zero from all possible destinations at once.

**Expand each cell only once**

Pop a cell and inspect its four valid neighbors. When a neighbor still has distance `-1`, assign the current distance plus one and enqueue it. An already assigned neighbor is never enqueued again.

**Why the first assigned distance is minimal**

Multi-source BFS processes cells in nondecreasing distance from the entire source set. Any path reaching an unvisited neighbor through the current cell has length `current + 1`; a shorter path would have placed that neighbor in an earlier BFS layer already. Thus the first assignment equals its shortest distance to any zero, and every reachable cell is eventually assigned.

#### Complexity detail

Each of the `rows * cols` cells enters the queue at most once and examines four neighbors, giving $O(rows \cdot cols)$ time. The distance matrix and queue use $O(rows \cdot cols)$ space.

#### Alternatives and edge cases

- **Two-pass dynamic programming:** propagates distances from top/left and then bottom/right with the same $O(rows \cdot cols)$ time and output storage.
- **BFS from every one:** is correct but repeatedly explores the matrix and can take quadratic time in the number of cells.
- **Check every zero for every cell:** is simple Manhattan-distance enumeration but costs $O(rows \cdot cols \cdot zero_count)$.
- **Zero cell:** always has distance zero and begins in the queue.
- **One row or column:** distances reduce to nearest-zero gaps along a line.
- **Several zeros:** simultaneous sources automatically select the closest one.
- **Rectangular matrix:** row and column bounds must use their separate dimensions.

</details>
