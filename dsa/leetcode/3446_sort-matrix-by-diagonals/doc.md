# Sort Matrix by Diagonals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3446 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sort-matrix-by-diagonals](https://leetcode.com/problems/sort-matrix-by-diagonals/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sort-matrix-by-diagonals/).

### Goal
Given an $n \times n$ square matrix, rearrange its elements such that every diagonal starting from the bottom-left to the top-right is sorted. Specifically, diagonals starting from the first column (bottom to top) and the first row (excluding the first column, left to right) must be sorted in non-decreasing order.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing an $n \times n$ square matrix.

**Return value**

- A list of lists of integers representing the modified matrix where each diagonal is sorted.

### Examples
**Example 1**

- Input: `grid = [[1,7,3],[9,8,2],[4,5,6]]`
- Output: `[[1,2,3],[4,5,6],[7,8,9]]`

**Example 2**

- Input: `grid = [[0,1],[1,2]]`
- Output: `[[0,1],[1,2]]`

**Example 3**

- Input: `grid = [[1]]`
- Output: `[[1]]`

---

## Solution
### Approach
The problem relies on the property that elements on the same diagonal share a constant difference between their row and column indices (`row - col`). By grouping elements by this constant `k = row - col`, we can extract all elements belonging to the same diagonal, sort them, and then re-insert them back into their respective positions in the matrix.

### Complexity Analysis
- **Time Complexity**: $O(n^2 \log n)$, where $n$ is the dimension of the matrix. We visit each of the $n^2$ elements to group them, and sorting each diagonal takes $O(k \log k)$ where $k$ is the length of the diagonal. Summing these results in $O(n^2 \log n)$.
- **Space Complexity**: $O(n^2)$ to store the elements of the diagonals in a hash map or dictionary before sorting and re-insertion.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)

    def sort_diagonal(row: int, col: int, reverse: bool) -> None:
        cells = []
        r, c = row, col
        while r < n and c < n:
            cells.append((r, c))
            r += 1
            c += 1
        values = sorted((grid[r][c] for r, c in cells), reverse=reverse)
        for (r, c), value in zip(cells, values):
            grid[r][c] = value

    for row in range(n):
        sort_diagonal(row, 0, True)
    for col in range(1, n):
        sort_diagonal(0, col, False)

    return grid
```
</details>
