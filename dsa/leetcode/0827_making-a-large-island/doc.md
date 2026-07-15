# Making A Large Island

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 827 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/making-a-large-island/) |

## Problem Description

### Goal

You are given an $n \times n$ binary matrix `grid`. An island is a group of cells containing `1` that are connected 4-directionally: consecutive cells share a horizontal or vertical side, while diagonal contact alone does not connect them. The size of an island is its number of cells.

You may change at most one cell containing `0` into `1`. Choose whether and where to apply that operation so that the resulting grid contains an island as large as possible. Return the size of that largest island. If the grid already contains only `1` cells, the unchanged whole grid is the answer.

### Function Contract

**Inputs**

- `grid`: an $n \times n$ matrix whose entries are `0` or `1`, where $1 \le n \le 500$

**Return value**

- The maximum size of a 4-directionally connected island after changing at most one `0` to `1`

### Examples

**Example 1**

- Input: `grid = [[1, 0], [0, 1]]`
- Output: `3`
- Explanation: Changing either `0` that touches both existing `1` cells joins them through the new land cell.

**Example 2**

- Input: `grid = [[1, 1], [1, 0]]`
- Output: `4`
- Explanation: Changing the only `0` extends the existing island to the entire grid.

**Example 3**

- Input: `grid = [[1, 1], [1, 1]]`
- Output: `4`
- Explanation: There is no `0` to change, and the existing island already occupies all four cells.

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Give every existing island a reusable identity**

Scan the grid once. Whenever an unvisited `1` appears, run an iterative depth-first search through its 4-directional neighbors. Write a new component label into a parallel matrix and count the component's cells. Store the resulting size under that label. After this pass, every land cell identifies its complete island in constant time, and no island needs to be traversed again for each possible change.

**Evaluate a water cell by merging distinct neighboring islands**

Changing a `0` at `(row, column)` creates one land cell. Its resulting island consists of that cell plus every existing island touching it above, below, left, or right. Collect the neighboring component labels in a set, then compute `1 + sum(sizes[label] for label in neighboring_labels)`. The set is essential: one bent or surrounding island may touch the same water cell from several directions but must contribute its size only once.

**Why checking local labels finds the global optimum**

Any newly connected path through the changed cell must enter one of its four neighbors, so the local label set includes every island that the operation can join. Conversely, every island represented by one of those labels becomes connected through the new cell. The candidate sum is therefore exactly the island created by that change. Taking the maximum over every `0`, while also retaining the largest unchanged component, covers every allowed choice because the operation is optional and affects at most one cell.

An all-water grid produces candidate size `1` for each cell. An all-land grid has no candidate changes, but the component-labeling pass records the existing size $n^2$.

#### Complexity detail

There are $n^2$ cells. Component labeling visits each cell and each of its at most four neighbor edges a constant number of times. The second scan also checks at most four labels per cell, so the total time is $O(n^2)$. The label matrix, component-size table, and worst-case traversal stack use $O(n^2)$ auxiliary space.

#### Alternatives and edge cases

- **Disjoint-set union:** Union adjacent land cells, store each root's size, and combine distinct roots around every `0`. It has near-linear time and $O(n^2)$ space but requires careful root deduplication.
- **Flip then flood-fill repeatedly:** Trying every `0` and recomputing all islands from scratch is correct but can take $O(n^4)$ time.
- **Recursive depth-first search:** It expresses component labeling compactly, but an island may contain $250{,}000$ cells and exceed Python's recursion limit; an explicit stack is safer.
- **All land:** Since the operation is optional and no `0` exists, return $n^2$.
- **All water:** Any one changed cell forms an island of size `1`.
- **Repeated neighboring label:** A single island touching the changed cell on multiple sides is added once, not once per side.
- **Diagonal land:** Diagonal cells remain disconnected unless a 4-directional path joins them.
- **Boundary cell:** Ignore neighbor coordinates outside the square rather than treating them as water components.

</details>
