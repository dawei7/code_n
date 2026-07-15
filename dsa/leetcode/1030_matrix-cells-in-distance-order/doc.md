# Matrix Cells in Distance Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1030 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Geometry, Sorting, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/matrix-cells-in-distance-order/) |

## Problem Description

### Goal

You are given a matrix with `rows` rows and `cols` columns and a starting cell `(rCenter, cCenter)` inside that matrix.

Return the coordinates of every matrix cell, ordered from the smallest Manhattan distance to the largest Manhattan distance from the center. For cells ((r_1,c_1)) and ((r_2,c_2)), that distance is
$$
\lvert r_1-r_2\rvert+\lvert c_1-c_2\rvert.
$$
Cells at the same distance may appear in any relative order.

### Function Contract

**Inputs**

- `rows`: the number of matrix rows, where $1 \le \texttt{rows} \le 100$.
- `cols`: the number of matrix columns, where $1 \le \texttt{cols} \le 100$.
- `r_center`: the center row, where $0 \le \texttt{r_center} < \texttt{rows}$.
- `c_center`: the center column, where $0 \le \texttt{c_center} < \texttt{cols}$.
- Let $M=\texttt{rows}\cdot\texttt{cols}$ be the number of cells.

**Return value**

- All $M$ coordinate pairs `[row, col]` in non-decreasing Manhattan-distance order.

### Examples

**Example 1**

- Input: `rows = 1, cols = 2, r_center = 0, c_center = 0`
- Output: `[[0,0],[0,1]]`
- Explanation: The two distances are $0$ and $1$.

**Example 2**

- Input: `rows = 2, cols = 2, r_center = 0, c_center = 1`
- Output: `[[0,1],[0,0],[1,1],[1,0]]`
- Explanation: The distances are $0,1,1,2$; the two distance-one cells may be exchanged.

**Example 3**

- Input: `rows = 2, cols = 3, r_center = 1, c_center = 2`
- Output: `[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]`
- Explanation: The distances are $0,1,1,2,2,3$, and other orders within equal-distance groups are valid.

### Required Complexity

- **Time:** $O(M)$
- **Space:** $O(M)$

<details>
<summary>Approach</summary>

#### General

**Bound the possible distance:** The farthest two cells in a `rows` by `cols` matrix differ by at most `rows - 1` vertically and `cols - 1` horizontally. Every center-to-cell distance is therefore an integer from $0$ through `rows + cols - 2`.

**Group cells by exact distance:** Allocate one bucket for each possible distance. Visit every coordinate `[row, col]`, compute `distance = abs(row - r_center) + abs(col - c_center)`, and append the coordinate to that bucket.

**Emit buckets in increasing order:** Concatenating bucket zero, bucket one, and so on includes every cell exactly once. All coordinates in an earlier bucket have a smaller distance than all coordinates in a later bucket; ties remain unrestricted, so the result satisfies the complete ordering contract.

#### Complexity detail

Computing and storing a bucket for each of the $M$ cells takes $O(M)$ time. The number of buckets is `rows + cols - 1`, which is $O(M)$ for positive dimensions, and flattening them visits $M$ entries. The buckets and returned coordinates use $O(M)$ space.

#### Alternatives and edge cases

- **Comparison sorting:** Enumerate all cells and sort by Manhattan distance. This is concise but takes $O(M\log M)$ time.
- **Breadth-first expansion:** Start from the center and visit unvisited orthogonal neighbors by layers. It is also $O(M)$ but needs a visited structure and queue.
- **Diamond-ring generation:** Generate only in-bounds points at each exact radius. It avoids sorting but requires careful handling of corners and duplicate axis points.
- **Single cell:** A `1 x 1` matrix returns only the center at distance zero.
- **Equal distances:** Their relative order is deliberately unspecified and must not be overconstrained.
- **Edge or corner center:** Buckets naturally omit coordinates outside the matrix without special distance rules.

</details>
