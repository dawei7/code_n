# Number of Closed Islands

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1254 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-closed-islands/) |

## Problem Description

### Goal

You are given a rectangular binary `grid` in which `0` represents land and `1` represents water. An island is a maximal group of land cells connected horizontally or vertically; diagonal contact does not connect two land cells.

A closed island is an island completely surrounded by water, which means none of its land cells can reach the outer boundary of the grid through other land cells. Return the number of closed islands. The input dimensions are at least large enough to contain an interior region.

### Function Contract

**Inputs**

- `grid`: an $m \times n$ matrix containing only `0` and `1`, where $1 \le m,n \le 100$.
- Let $N=mn$ be the total number of cells.

**Return value**

- Return the number of four-directionally connected land components that do not touch the grid boundary.

### Examples

**Example 1**

- Input: `grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]`
- Output: `2`

**Example 2**

- Input: `grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]`
- Output: `1`

**Example 3**

- Input: `grid = [[1,1,1],[1,0,1],[1,1,1]]`
- Output: `1`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

Traverse every cell and start a flood fill whenever unvisited land is found. During that one traversal, mark every land cell in the same four-directional component so the outer scan never starts a second search for the same island.

**Detecting whether a component is open**

Initialize the component as closed. When flood fill visits a land cell on row zero, row $m-1$, column zero, or column $n-1$, mark the component as open. Continue visiting the rest of the component even after finding a boundary cell, because all of its cells still need to be marked to prevent duplicate work.

**Counting each island exactly once**

Changing visited land from `0` to `1` provides an in-place visited marker. Each original land cell is therefore discovered by exactly one flood fill. After that fill finishes, increment the answer only if no visited cell touched the boundary. Water cells and already visited cells require no further work.

An explicit stack avoids relying on recursion depth for a component that may contain every grid cell. Mutating the working grid is safe for the app runner's isolated case input and uses the matrix itself as the visited structure.

#### Complexity detail

Every one of the $N$ cells is inspected a constant number of times, giving $O(N)$ time. The explicit stack can contain $O(N)$ land cells in the worst case, so auxiliary space is $O(N)$.

#### Alternatives and edge cases

- **Erase boundary land first:** Flood-fill every boundary-connected island, then count the remaining components; this is also linear and makes the final counting pass especially direct.
- **Union-find:** Join adjacent land cells and a virtual boundary node, then count roots not connected to the boundary; it is correct but uses more bookkeeping.
- **Fresh search from every land cell:** Without a global visited marker, one large island can be traversed repeatedly and require $O(N^2)$ time.
- **All water:** No flood fill starts, so the answer is zero.
- **All land:** The single island touches the boundary and is not closed.
- **Diagonal land contact:** Diagonal cells remain separate components unless a horizontal or vertical land path connects them.

</details>
