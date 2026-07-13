# Maximum Score From Grid Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3225 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-score-from-grid-operations](https://leetcode.com/problems/maximum-score-from-grid-operations/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-score-from-grid-operations/).

### Goal
Given an $n \times n$ grid of non-negative integers, you must select a set of cells to "paint" such that the resulting shape is formed by a sequence of non-increasing column heights from left to right, followed by a sequence of non-decreasing column heights. Specifically, for each column $j$, you choose a height $h_j$ (number of cells from the top), and the score is the sum of all values in the grid that are *not* painted. The goal is to maximize this score by choosing an optimal configuration of heights.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers of size $n \times n$.

**Return value**

- An integer representing the maximum possible sum of the unpainted cells.

### Examples
**Example 1**

- Input: `grid = [[0,0,0,0,0],[0,0,3,0,0],[0,2,0,0,2],[0,0,0,0,1],[0,0,0,0,0]]`
- Output: `11`

**Example 2**

- Input: `grid = [[10,10,10],[10,10,10],[10,10,10]]`
- Output: `0`

---

## Solution
### Approach
The problem is solved using Dynamic Programming with state compression. We define `dp[col][prev_h][state]` where `col` is the current column, `prev_h` is the height of the previous column, and `state` is a boolean indicating whether we are currently in the "non-increasing" phase or the "non-decreasing" phase. We use prefix sums to calculate the sum of grid values in a column segment in $O(1)$ time.

### Complexity Analysis
- **Time Complexity**: $O(n^3)$, where $n$ is the dimension of the grid. We iterate through $n$ columns, and for each, we iterate through possible heights $h$ and $prev\_h$.
- **Space Complexity**: $O(n^2)$ to store the DP table and the prefix sum array.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[int]]) -> int:
    n = len(grid)
    height_count = n + 1

    col_prefix = [[0] * height_count for _ in range(n)]
    for col in range(n):
        for row in range(n):
            col_prefix[col][row + 1] = col_prefix[col][row] + grid[row][col]

    def column_score(col: int, height: int, neighbor_height: int) -> int:
        if neighbor_height <= height:
            return 0
        return col_prefix[col][neighbor_height] - col_prefix[col][height]

    if n == 1:
        return 0

    dp = [[-10**30] * height_count for _ in range(height_count)]
    for h0 in range(height_count):
        for h1 in range(height_count):
            dp[h0][h1] = column_score(0, h0, h1)

    for col in range(1, n - 1):
        new_dp = [[-10**30] * height_count for _ in range(height_count)]
        pref = col_prefix[col]

        for current in range(height_count):
            best_prev_at_most = [-10**30] * height_count
            running = -10**30
            for previous in range(height_count):
                running = max(running, dp[previous][current])
                best_prev_at_most[previous] = running

            best_prev_more = [-10**30] * (height_count + 1)
            running = -10**30
            for previous in range(height_count - 1, -1, -1):
                extra = pref[previous] - pref[current] if previous > current else 0
                running = max(running, dp[previous][current] + extra)
                best_prev_more[previous] = running

            for next_height in range(height_count):
                from_left_neighbor = best_prev_at_most[next_height] + column_score(col, current, next_height)
                from_right_neighbor = best_prev_more[next_height + 1]
                new_dp[current][next_height] = max(from_left_neighbor, from_right_neighbor)

        dp = new_dp

    answer = 0
    last_col = n - 1
    for previous in range(height_count):
        for current in range(height_count):
            answer = max(answer, dp[previous][current] + column_score(last_col, current, previous))
    return answer
```
</details>
