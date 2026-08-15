# Check if Grid Satisfies Conditions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3142 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-grid-satisfies-conditions/) |

## Problem Description

### Goal

You are given an $m \times n$ integer matrix `grid`. Decide whether every cell obeys both adjacency rules that apply to it.

A cell must equal the cell immediately below it whenever that lower neighbor exists. It must also differ from the cell immediately to its right whenever that right neighbor exists. Return `True` exactly when all cells satisfy every applicable rule; otherwise return `False`.

### Function Contract

**Inputs**

- `grid`: A nonempty rectangular list of integer rows.

Let $m$ be the number of rows and $n$ the number of columns. The constraints are $1 \le m,n \le 10$ and $0 \le \texttt{grid[i][j]} \le 9$.

**Return value**

Return `True` if each vertical pair contains equal values and each horizontal pair contains different values. Return `False` otherwise.

### Examples

#### Example 1

- **Input:** `grid = [[1, 0, 2], [1, 0, 2]]`
- **Output:** `True`
- **Explanation:** Each column is constant from top to bottom, and neighboring columns have different values.

#### Example 2

- **Input:** `grid = [[1, 1, 1], [0, 0, 0]]`
- **Output:** `False`
- **Explanation:** The first row contains equal horizontal neighbors, so the required difference does not hold.

#### Example 3

- **Input:** `grid = [[1], [2], [3]]`
- **Output:** `False`
- **Explanation:** The cells in the only column are not all equal.
