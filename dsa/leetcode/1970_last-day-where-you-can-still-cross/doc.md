# Last Day Where You Can Still Cross

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1970 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/last-day-where-you-can-still-cross/) |

## Problem Description
### Goal
A 1-based binary matrix has `row` rows and `col` columns. Every cell is land
on day `0`. Thereafter, exactly one new cell becomes water per day according
to the permutation `cells`: entry `cells[i]` gives the 1-based row and column
flooded on day `i + 1`.

On a given day, crossing is possible when a path of land cells starts anywhere
in the top row, ends anywhere in the bottom row, and moves only up, down, left,
or right. Return the latest day number on which such a top-to-bottom path still
exists.

### Function Contract
**Inputs**

- `row`: the number of matrix rows, where $2 \le \texttt{row} \le 2\cdot10^4$.
- `col`: the number of matrix columns, where
  $2 \le \texttt{col} \le 2\cdot10^4$.
- `cells`: all $N=\texttt{row}\cdot\texttt{col}$ distinct matrix coordinates
  in their flooding order, with $4 \le N \le 2\cdot10^4$.

**Return value**

- The greatest day in the range from `0` through `N` for which a land-only
  top-to-bottom crossing exists after that day's flooding.

### Examples
**Example 1**

- Input: `row = 2, col = 2, cells = [[1, 1], [2, 1], [1, 2], [2, 2]]`
- Output: `2`

**Example 2**

- Input: `row = 2, col = 2, cells = [[1, 1], [1, 2], [2, 1], [2, 2]]`
- Output: `1`

**Example 3**

- Input: `row = 3, col = 3, cells = [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]`
- Output: `3`

### Required Complexity
- **Time:** $O(N\alpha(N))$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Reverse flooding into land activation**

After the final day every cell is water. Process `cells` backward, turning one
cell back into land at each step. Maintain connected components of activated
land cells with a disjoint-set union structure. A cell is joined to each
active cardinal neighbor.

Add two virtual nodes: one represents the top boundary and the other the
bottom boundary. Join every activated top-row cell to the top node and every
activated bottom-row cell to the bottom node. A crossing exists exactly when
these two virtual nodes belong to the same component.

**Translate the first reverse connection into the last forward day**

Suppose reverse processing activates `cells[day]`. The active cells are then
precisely those that remain land after the first `day` forward floods. If the
virtual boundaries become connected at this moment, day `day` is crossable.

Later reverse steps correspond to earlier forward days and can only add land,
so connectivity cannot disappear. The first reverse connection is therefore
the latest crossable forward day. Union-find cannot invent a path: every union
represents either a real cardinal land adjacency or a cell touching the
appropriate boundary. Conversely, every land path is joined edge by edge, so
an actual crossing necessarily connects the virtual nodes.

#### Complexity detail

Here $N=\texttt{row}\cdot\texttt{col}$. Each cell is activated once and causes
at most six union operations: four neighbors and up to two virtual
boundaries. Union by size with path compression gives $O(N\alpha(N))$ total
time. The parent, component-size, and active-cell arrays use $O(N)$ space.

#### Alternatives and edge cases

- **Binary search plus BFS or DFS:** Crossability is monotone over days, so
  search for the last true day and traverse the grid for every probe. This is
  correct but costs $O(N\log N)$ time.
- **Test every day forward:** Flood one cell and rerun a complete traversal.
  This can take $O(N^2)$ time.
- **Diagonal movement:** Diagonally touching land cells are not connected;
  only four cardinal directions are legal.
- Coordinates in `cells` are 1-based, whereas flattened array indices are
  naturally 0-based. Convert both coordinates before computing the index.
- Any dry top-row cell may start the path and any dry bottom-row cell may end
  it; no particular column must remain open.
- The returned day counts completed floods. It is not the zero-based index of
  the last dry cell in `cells`, although those values coincide in the reverse
  activation step used by the algorithm.

</details>
