# Maximum Strictly Increasing Cells in a Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2713 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Dynamic Programming, Memoization, Sorting, Matrix, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-strictly-increasing-cells-in-a-matrix](https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/).

### Goal
Given an $m \times n$ matrix of integers, find the maximum number of cells you can visit by moving from cell to cell. From any cell, you can move to any other cell in the same row or same column, provided that the value of the destination cell is strictly greater than the value of the current cell. You can start your path at any cell in the matrix.

### Function Contract
**Inputs**

- `mat`: `List[List[int]]` - A 2D grid of size $m \times n$ containing integers.

**Return value**

- `int` - The maximum number of cells that can be visited in a valid path.

### Examples
**Example 1**

- Input: `mat = [[3, 1], [3, 4]]`
- Output: `2`
- Explanation: One optimal path is `(0, 1) -> (1, 1)` with values `1 -> 4`. Another is `(0, 1) -> (0, 0)` with values `1 -> 3`.

**Example 2**

- Input: `mat = [[1, 1], [1, 1]]`
- Output: `1`
- Explanation: Since all values are equal, we cannot make any valid moves. The maximum path length is 1.

**Example 3**

- Input: `mat = [[3, 1, 6], [-9, 5, 7]]`
- Output: `4`
- Explanation: An optimal path is `(1, 0) -> (0, 1) -> (1, 1) -> (1, 2)` with values `-9 -> 1 -> 5 -> 7`.

---

## Solution
### Approach
The problem can be modeled as finding the longest path in a Directed Acyclic Graph (DAG), where each cell is a node, and a directed edge exists from cell $A$ to cell $B$ if they are in the same row or column and $val(A) < val(B)$.

Since the transitions must be strictly increasing, we can process the cells in increasing order of their values. This allows us to use Dynamic Programming (DP) with memoization or iterative DP.
To optimize the transitions:
1. Group all cell coordinates by their matrix values.
2. Sort these unique values in ascending order.
3. Maintain two arrays: `row_max` of size $m$ and `col_max` of size $n$, where `row_max[i]` stores the maximum path length ending in row $i$ so far, and `col_max[j]` stores the maximum path length ending in column $j$ so far.
4. For each unique value, compute the potential DP value for all cells containing this value:
   $$\text{dp}[r][c] = \max(\text{row\_max}[r], \text{col\_max}[c]) + 1$$
5. After computing the DP values for all cells of the current value, update the `row_max` and `col_max` arrays with these new DP values. This step is deferred until all cells of the same value are processed to ensure we only transition from strictly smaller values.
6. The final answer is the maximum value in `row_max` or `col_max`.

### Complexity Analysis
- **Time Complexity**: $O(M \times N \log(M \times N))$ where $M$ is the number of rows and $N$ is the number of columns. Grouping the cells takes $O(M \times N)$ time, and sorting the unique values takes $O(U \log U)$ where $U \le M \times N$ is the number of unique values. Processing each cell takes $O(1)$ time.
- **Space Complexity**: $O(M \times N)$ to store the coordinates of the cells grouped by their values. The auxiliary space for `row_max` and `col_max` is $O(M + N)$.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict
from typing import List

def solve(mat: List[List[int]]) -> int:
    m, n = len(mat), len(mat[0])
    val_to_coords = defaultdict(list)
    for r in range(m):
        for c in range(n):
            val_to_coords[mat[r][c]].append((r, c))

    row_max = [0] * m
    col_max = [0] * n

    for val in sorted(val_to_coords.keys()):
        coords = val_to_coords[val]
        # Store the new dp values for this batch
        updates = []
        for r, c in coords:
            dp_val = max(row_max[r], col_max[c]) + 1
            updates.append((r, c, dp_val))

        # Apply updates to row_max and col_max
        for r, c, dp_val in updates:
            row_max[r] = max(row_max[r], dp_val)
            col_max[c] = max(col_max[c], dp_val)

    return max(max(row_max), max(col_max))
```
</details>
