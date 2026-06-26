# Difference Between Ones and Zeros in Row and Column

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2482 |
| Difficulty | Medium |
| Topics | Array, Matrix, Simulation |
| Official Link | [difference-between-ones-and-zeros-in-row-and-column](https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/) |

## Problem Description & Examples
### Goal
Given a 0-indexed $m \times n$ binary matrix `grid`, construct a 0-indexed $m \times n$ difference matrix `diff`. 

For each cell `(i, j)` in the matrix, the value `diff[i][j]` is calculated as:
$$\text{diff}[i][j] = \text{onesRow}_i + \text{onesCol}_j - \text{zerosRow}_i - \text{zerosCol}_j$$

Where:
- $\text{onesRow}_i$ is the number of ones in the $i$-th row.
- $\text{onesCol}_j$ is the number of ones in the $j$-th column.
- $\text{zerosRow}_i$ is the number of zeros in the $i$-th row.
- $\text{zerosCol}_j$ is the number of zeros in the $j$-th column.

Return the resulting difference matrix `diff`.

### Function Contract
**Inputs**

- `grid`: `List[List[int]]` - A 2D grid of size $m \times n$ containing only `0`s and `1`s.

**Return value**

- `List[List[int]]` - The $m \times n$ difference matrix `diff`.

### Examples
**Example 1**

- **Input**: `grid = [[0,1,1],[1,0,1],[0,0,1]]`
- **Output**: `[[0,0,4],[0,0,4],[-2,-2,2]]`
- **Explanation**:
  - Row 0: ones = 2, zeros = 1
  - Row 1: ones = 2, zeros = 1
  - Row 2: ones = 1, zeros = 2
  - Col 0: ones = 1, zeros = 2
  - Col 1: ones = 1, zeros = 2
  - Col 2: ones = 3, zeros = 0
  - `diff[0][0] = 2 + 1 - 1 - 2 = 0`
  - `diff[0][1] = 2 + 1 - 1 - 2 = 0`
  - `diff[0][2] = 2 + 3 - 1 - 0 = 4`
  - `diff[1][0] = 2 + 1 - 1 - 2 = 0`
  - `diff[1][1] = 2 + 1 - 1 - 2 = 0`
  - `diff[1][2] = 2 + 3 - 1 - 0 = 4`
  - `diff[2][0] = 1 + 1 - 2 - 2 = -2`
  - `diff[2][1] = 1 + 1 - 2 - 2 = -2`
  - `diff[2][2] = 1 + 3 - 2 - 0 = 2`

**Example 2**

- **Input**: `grid = [[1,1,1],[1,1,1]]`
- **Output**: `[[5,5,5],[5,5,5]]`
- **Explanation**:
  - Row 0: ones = 3, zeros = 0
  - Row 1: ones = 3, zeros = 0
  - Col 0: ones = 2, zeros = 0
  - Col 1: ones = 2, zeros = 0
  - Col 2: ones = 2, zeros = 0
  - `diff[i][j] = 3 + 2 - 0 - 0 = 5` for all cells.

---

## Underlying Base Algorithm(s)
The naive approach of counting ones and zeros for every cell independently results in an inefficient $O(m \cdot n \cdot (m + n))$ time complexity. 

To optimize this, we can precompute the counts of ones for each row and column. Since the grid only contains `0`s and `1`s, we can derive the number of zeros directly from the dimensions of the grid:
- $\text{zerosRow}_i = n - \text{onesRow}_i$
- $\text{zerosCol}_j = m - \text{onesCol}_j$

Substituting these into the original formula:
$$\text{diff}[i][j] = \text{onesRow}_i + \text{onesCol}_j - (n - \text{onesRow}_i) - (m - \text{onesCol}_j)$$
$$\text{diff}[i][j] = 2 \cdot \text{onesRow}_i + 2 \cdot \text{onesCol}_j - m - n$$

By precomputing `onesRow` and `onesCol` in a single pass over the grid, we can construct the final matrix in $O(1)$ time per cell.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(m \cdot n)$ where $m$ is the number of rows and $n$ is the number of columns. We traverse the grid once to count the ones, and once more to populate the `diff` matrix.
- **Space Complexity**: $\mathcal{O}(m + n)$ auxiliary space to store the precomputed row and column counts. The output matrix itself takes $\mathcal{O}(m \cdot n)$ space.
