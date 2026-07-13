# Minimum Number of Operations to Satisfy Conditions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3122 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-operations-to-satisfy-conditions](https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/).

### Goal
Given a 2D grid of integers, determine the minimum number of cell modifications required to ensure that every column contains only one unique value, and that no two adjacent columns contain the same unique value.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing the input matrix of dimensions `m x n`.

**Return value**

- An integer representing the minimum number of operations (changing a cell's value) to satisfy the column constraints.

### Examples
**Example 1**

- Input: `grid = [[1,0,2],[1,0,2]]`
- Output: `0`

**Example 2**

- Input: `grid = [[1,1,1],[0,0,0]]`
- Output: `3`

**Example 3**

- Input: `grid = [[1],[2],[3]]`
- Output: `0`

---

## Solution
### Approach
Dynamic Programming. We first pre-calculate the cost to make each column consist entirely of a specific digit (0-9). Then, we define `dp[col][val]` as the minimum cost to satisfy the conditions for all columns up to `col`, where `col` is assigned the digit `val`. The transition is `dp[col][val] = cost[col][val] + min(dp[col-1][prev_val])` for all `prev_val != val`.

### Complexity Analysis
- **Time Complexity**: `O(n * 10^2)`, where `n` is the number of columns. Since the number of possible values is fixed at 10, this simplifies to `O(n)`.
- **Space Complexity**: `O(n * 10)`, which simplifies to `O(n)` to store the DP table.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    # Precompute cost to make each column 'j' consist entirely of digit 'v'
    # cost[j][v] = m - (count of v in column j)
    costs = [[m for _ in range(10)] for _ in range(n)]
    for j in range(n):
        counts = [0] * 10
        for i in range(m):
            counts[grid[i][j]] += 1
        for v in range(10):
            costs[j][v] = m - counts[v]

    # dp[v] stores the min cost to satisfy columns up to current,
    # ending with the current column having value 'v'
    dp = [costs[0][v] for v in range(10)]

    for j in range(1, n):
        new_dp = [float('inf')] * 10
        # To optimize finding the min of previous dp excluding current v:
        # Find the two smallest values in the previous dp table
        first_min = float('inf')
        second_min = float('inf')
        first_idx = -1

        for v in range(10):
            if dp[v] < first_min:
                second_min = first_min
                first_min = dp[v]
                first_idx = v
            elif dp[v] < second_min:
                second_min = dp[v]

        for v in range(10):
            prev_min = second_min if v == first_idx else first_min
            new_dp[v] = costs[j][v] + prev_min
        dp = new_dp

    return min(dp)
```
</details>
