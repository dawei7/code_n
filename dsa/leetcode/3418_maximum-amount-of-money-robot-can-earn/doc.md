# Maximum Amount of Money Robot Can Earn

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3418 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-amount-of-money-robot-can-earn](https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/).

### Goal
Calculate the maximum profit a robot can accumulate while traversing a grid from the top-left corner to the bottom-right corner. The robot can only move right or down. Each cell contains a monetary value (which can be negative). The robot is granted a special ability to "neutralize" up to two negative-value cells, effectively treating their value as zero.

### Function Contract
**Inputs**

- `coins`: A 2D list of integers representing the grid of monetary values.

**Return value**

- An integer representing the maximum possible sum of coins collected from (0, 0) to (m-1, n-1) given the ability to ignore up to two negative values.

### Examples
**Example 1**

- Input: `coins = [[0,1,-1],[1,-2,3]]`
- Output: `8`

**Example 2**

- Input: `coins = [[1,-1,-1,1]]`
- Output: `1`

**Example 3**

- Input: `coins = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]`
- Output: `0`

---

## Solution
### Approach
Dynamic Programming with State Compression. We maintain a 3D DP table `dp[i][j][k]`, where `i, j` are the grid coordinates and `k` (0 to 2) represents the number of negative values already neutralized.

### Complexity Analysis
- **Time Complexity**: O(M * N), where M is the number of rows and N is the number of columns, as we visit each cell and perform a constant number of operations (3 states for k).
- **Space Complexity**: O(M * N), which can be optimized to O(N) since each state only depends on the previous row/column.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(coins: list[list[int]]) -> int:
    rows = len(coins)
    cols = len(coins[0])

    # dp[i][j][k] = max money at (i, j) having neutralized k negative values
    # Initialize with negative infinity to represent unreachable states
    inf = float('inf')
    dp = [[[ -inf for _ in range(3)] for _ in range(cols)] for _ in range(rows)]

    # Base case: starting cell
    val = coins[0][0]
    if val < 0:
        dp[0][0][0] = val
        dp[0][0][1] = 0
    else:
        dp[0][0][0] = val

    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                continue

            # Possible previous cells
            prevs = []
            if i > 0: prevs.append(dp[i-1][j])
            if j > 0: prevs.append(dp[i][j-1])

            curr_val = coins[i][j]

            for prev_dp in prevs:
                for k in range(3):
                    if prev_dp[k] == -inf:
                        continue

                    # Option 1: Don't neutralize current cell
                    dp[i][j][k] = max(dp[i][j][k], prev_dp[k] + curr_val)

                    # Option 2: Neutralize current cell if it's negative and we have charges left
                    if curr_val < 0 and k < 2:
                        dp[i][j][k+1] = max(dp[i][j][k+1], prev_dp[k])

    return max(dp[rows-1][cols-1])
```
</details>
