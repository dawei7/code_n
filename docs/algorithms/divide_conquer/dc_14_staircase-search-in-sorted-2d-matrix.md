# Search a 2D Matrix (Staircase Search)

| | |
|---|---|
| **ID** | `dc_14` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N + M)$ Time, $O(1)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) |

## Problem statement

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:
- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

**Input:** A 2D matrix of dimensions M x N, and a `target` integer.
**Output:** A boolean representing whether the target is present.

## When to use it

- A highly frequent matrix traversal problem.
- To demonstrate how to use properties of two-dimensional sorting to mathematically discard entire rows or columns in $O(1)$ time per step.

## Approach

**1. The Flaw of Binary Search:**
Because the rows are sorted, we could just run a 1D Binary Search on every single row! This would take $O(M log N)$ time.
But wait! The columns are ALSO sorted. Can we use both properties simultaneously?

**2. The Staircase Approach (Decrease and Conquer):**
Look at the **Top-Right** corner of the matrix.
Let's say the matrix is:
```text
 1   4   7  11
 2   5   8  12
 3   6   9  16
```
The Top-Right element is `11`. Let our `target` be `5`.
If we compare `target` to `11`, `5 < 11`.
Because the column is sorted strictly ascending from top to bottom, every number BELOW `11` in that column must be GREATER than `11`. Therefore, they must also be greater than `5`!
We can mathematically eliminate the ENTIRE LAST COLUMN! We move our pointer to the left (to `7`).

Now let's compare `target=5` to `7`. `5 < 7`. We eliminate the column again! Move left to `4`.
Compare `target=5` to `4`. `5 > 4`.
Because the row is sorted strictly ascending from left to right, every number to the LEFT of `4` in that row must be LESS than `4`. Therefore, they must also be less than `5`!
We can mathematically eliminate the ENTIRE FIRST ROW! We move our pointer down (to `5`).

Compare `target=5` to `5`. Match found!

**3. The Rules:**
Start at `row = 0`, `col = N - 1` (Top-Right).
- If `matrix[row][col] == target`: Return `True`.
- If `matrix[row][col] > target`: The target must be to the Left. `col -= 1`.
- If `matrix[row][col] < target`: The target must be Below. `row += 1`.
*(Note: You can also start at the Bottom-Left corner and apply the exact inverse logic! You CANNOT start Top-Left or Bottom-Right, because both valid directions would lead to larger/smaller numbers simultaneously, creating an ambiguous branch).*

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_14: Staircase Search in Sorted 2D Matrix.

Given an n x m matrix where each row and each
"""


def solve(matrix, n, m, target):
    """Staircase search from the top-right corner."""
    if n == 0 or m == 0:
        return False
    i, j = 0, m - 1
    while i < n and j >= 0:
        v = matrix[i][j]
        if v == target:
            return True
        if v > target:
            j -= 1
        else:
            i += 1
    return False
```

</details>

## Walk-through

`matrix` is 3 x 4 (above). `target = 6`.
Start `row = 0`, `col = 3` (val = 11).

1. `11 > 6`. Move Left. `col = 2`.
2. `matrix[0][2]` = 7. `7 > 6`. Move Left. `col = 1`.
3. `matrix[0][1]` = 4. `4 < 6`. Move Down. `row = 1`.
4. `matrix[1][1]` = 5. `5 < 6`. Move Down. `row = 2`.
5. `matrix[2][1]` = 6. `6 == 6`. MATCH!

Returns `True`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(M + N)$ | $O(1)$ |
| **Worst** | $O(M + N)$ | $O(1)$ |

In the worst case, the target is at the bottom-left corner, and the pointer must travel all the way across the top row (N steps) and all the way down the left column (M steps). The path taken is a "staircase" from top-right to bottom-left. Total steps cannot exceed M + N. Time complexity is strictly $O(M + N)$.
Space complexity is $O(1)$.

## Variants & optimizations

- **Pure Divide and Conquer (Quad-Tree):** Is $O(M+N)$ the fastest possible? For a square N x N matrix, it's $O(N)$. Can we do it in $O(\log N)$? Actually, no. But we can write a pure Divide and Conquer algorithm that checks the center element. It eliminates one of the 4 quadrants entirely, and recursively searches the other 3 quadrants. T(N) = 3T(N/2) -> $O(N^{log_2 3})$ ~= $O(N^{1.58})$. So the $O(M+N)$ Staircase approach is undeniably the mathematically optimal solution!
- **Search a 2D Matrix I (LeetCode 74):** A significantly easier variant where the LAST integer of a row is strictly less than the FIRST integer of the next row. The entire matrix is just one giant 1D sorted array folded over! You can just run a pure $O(log(MN)$) Binary Search using `row = mid // n` and `col = mid % n`.

## Real-world applications

- **Data Compression (Block Sorting):** Scanning structurally constrained 2D spatial blocks for quantization thresholds in JPEG/MPEG encoding algorithms.

## Related algorithms in cOde(n)

- **[searching_01 - Binary Search](../searching/search_01_binary-search.md)** — For solving the easier "Matrix I" variant.
- **[dc_03 - Kth Smallest Element (Quickselect)](dc_03_kth-smallest-quickselect.md)** — Another application of Decrease and Conquer where a fraction of the search space is deterministically discarded.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
