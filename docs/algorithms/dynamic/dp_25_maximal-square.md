# Maximal Square

| | |
|---|---|
| **ID** | `dp_25` |
| **Category** | dynamic |
| **Complexity (required)** | $O(M * N)$ Time, $O(N)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Maximal Square](https://leetcode.com/problems/maximal-square/) |

## Problem statement

Given an `m x n` binary matrix filled with `0`'s and `1`'s, find the largest square containing only `1`'s and return its area.

**Input:** An `m x n` matrix `matrix` where elements are chars `'0'` or `'1'`.
**Output:** An integer representing the area of the largest square.

## When to use it

- A classic 2D Grid DP problem that teaches you how to look UP, LEFT, and DIAGONAL-UP-LEFT to determine the state of the current cell.
- The perfect stepping stone before tackling the much harder `Maximal Rectangle` problem.

## Approach

**1. Define the State:**
Let `dp[i][j]` be the **side length** of the maximum square whose *bottom-right corner* is located exactly at cell `(i, j)`.

**2. Find the Base Cases:**
If we are in the first row (`i = 0`) or the first column (`j = 0`), the maximum square that can end there is limited to the cell itself!
If `matrix[i][j] == '1'`, then `dp[i][j] = 1`.
If `matrix[i][j] == '0'`, then `dp[i][j] = 0`.

**3. Find the Transition (The recurrence relation):**
For any internal cell `(i, j)`, what determines if it can form a larger square?
First, `matrix[i][j]` MUST be `'1'`. If it is `'0'`, the square is immediately broken, and `dp[i][j] = 0`.
If it IS `'1'`, it can act as the bottom-right corner of a larger square IF AND ONLY IF the three adjacent cells (Left, Up, Diagonal-Up-Left) ALSO form squares of at least a certain size!
The size of the square ending at `(i, j)` is constrained by the **smallest** of those three surrounding squares.
`dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`

We keep track of the `max_side` seen globally across the entire DP matrix. The final area is `max_side * max_side`.

**4. Optimize Space:**
Notice that `dp[i][j]` only relies on the current row `i` and the previous row `i-1`. We can optimize this from $O(M \times N)$ space down to a 1D array of size N!
We just need a temporary variable to hold `dp[i-1][j-1]` before it gets overwritten.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_25: Maximal Square.

dp[i][j] = side length of the largest square whose bottom-
right corner is at (i, j). Recurrence:
dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
if matrix[i][j] == '1', else 0. Space-optimized to O(N).
"""


def solve(matrix, m, n):
    if m == 0 or n == 0:
        return 0
    dp = [0] * (n + 1)
    max_side = 0
    prev = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            temp = dp[j]
            if matrix[i - 1][j - 1] == "1":
                dp[j] = min(dp[j], dp[j - 1], prev) + 1
                max_side = max(max_side, dp[j])
            else:
                dp[j] = 0
            prev = temp
        prev = 0
    return max_side * max_side
```

</details>

## Walk-through

`matrix = [["1","0","1","0"], ["1","1","1","1"], ["1","1","1","1"]]`
M=3, N=4. `dp` initialized to `[0, 0, 0, 0, 0]`.

1. **i = 1 (Row 0: `1 0 1 0`):**
   - `j=1 ('1')`: `dp[1] = min(0, 0, 0) + 1 = 1`. `max=1`.
   - `j=2 ('0')`: `dp[2] = 0`.
   - `j=3 ('1')`: `dp[3] = min(0, 0, 0) + 1 = 1`.
   - `j=4 ('0')`: `dp[4] = 0`.
   - `dp` state: `[0, 1, 0, 1, 0]`.

2. **i = 2 (Row 1: `1 1 1 1`):**
   - `j=1 ('1')`: `dp[1] = min(1(up), 0(left), 0(diag)) + 1 = 1`.
   - `j=2 ('1')`: `dp[2] = min(0(up), 1(left), 1(diag)) + 1 = 1`.
   - `j=3 ('1')`: `dp[3] = min(1(up), 1(left), 0(diag)) + 1 = 1`.
   - `j=4 ('1')`: `dp[4] = min(0(up), 1(left), 1(diag)) + 1 = 1`.
   - `dp` state: `[0, 1, 1, 1, 1]`.

3. **i = 3 (Row 2: `1 1 1 1`):**
   - `j=1 ('1')`: `dp[1] = 1`.
   - `j=2 ('1')`: `dp[2] = min(1, 1, 1) + 1 = 2`. `max=2`.
   - `j=3 ('1')`: `dp[3] = min(1, 2, 1) + 1 = 2`.
   - `j=4 ('1')`: `dp[4] = min(1, 2, 1) + 1 = 2`.
   - `dp` state: `[0, 1, 2, 2, 2]`.

Final `max_side` is 2. Area is 2 x 2 = 4. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(M * N)$ | $O(N)$ |
| **Average** | $O(M * N)$ | $O(N)$ |
| **Worst** | $O(M * N)$ | $O(N)$ |

The nested loops strictly visit every cell in the M x N matrix exactly once, doing $O(1)$ operations. Time is strictly $O(M \times N)$.
By using the 1D rolling array, Space is $O(N)$ (where N is the number of columns).

## Variants & optimizations

- **Count Square Submatrices with All Ones:** Instead of returning the MAXIMUM area, return the total NUMBER of valid squares! The logic is absolutely identical. The value `dp[i][j]` exactly represents how many valid squares have their bottom-right corner at `(i, j)`. You simply sum up all the `dp[i][j]` values across the entire matrix!
- **Maximal Rectangle:** What if the shape doesn't have to be a perfect square? The `min()` logic completely falls apart. This requires an entirely different approach using monotonic stacks! (`dp_26`).

## Real-world applications

- **Computer Vision:** Quickly identifying bounding boxes for dense, uniform-color regions (like a solid white wall or a block of text) in an image processing pipeline.

## Related algorithms in cOde(n)

- **[dp_12 - Minimum Path Sum](dp_12_min-cost-path.md)** — Another 2D Grid DP where you optimize a 1D row array, but here you must also track the diagonal state!
- **[dp_26 - Maximal Rectangle](dp_26_maximal-rectangle.md)** — The much harder variant where the width and height can differ.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
