# Minimum Total Distance Traveled

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2463 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-total-distance-traveled](https://leetcode.com/problems/minimum-total-distance-traveled/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-total-distance-traveled/).

### Goal
Given a set of robot positions on a 1D line and a set of factory locations, each with a specific repair capacity, assign each robot to a factory such that every robot is repaired and the total distance traveled by all robots is minimized. Each factory can only repair a limited number of robots.

### Function Contract
**Inputs**

- `robot`: A list of integers representing the 1D coordinates of each robot.
- `factory`: A list of lists, where each inner list `[position, limit]` represents the coordinate of a factory and the maximum number of robots it can repair.

**Return value**

- An integer representing the minimum total distance all robots must travel to reach their assigned factories.

### Examples
**Example 1**

- Input: `robot = [0,4,6], factory = [[2,2],[6,2]]`
- Output: `4`

**Example 2**

- Input: `robot = [1,-1], factory = [[-2,1],[2,1]]`
- Output: `2`

**Example 3**

- Input: `robot = [1,2,3], factory = [[1,1],[2,1],[3,1]]`
- Output: `0`

---

## Solution
### Approach
The problem is solved using Dynamic Programming. First, sort both the robots and the factories by their positions. We define `dp[i][j]` as the minimum cost to repair the first `i` robots using a subset of the first `j` factories. The transition involves deciding how many robots (from 0 up to the factory's limit) the `j`-th factory will repair.

### Complexity Analysis
- **Time Complexity**: `O(N * M * K)`, where `N` is the number of robots, `M` is the number of factories, and `K` is the maximum capacity of a factory. Given the constraints, this is efficient enough.
- **Space Complexity**: `O(N * M)` to store the DP table.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(robot: list[int], factory: list[list[int]]) -> int:
    robot.sort()
    factory.sort()

    n = len(robot)
    m = len(factory)

    # dp[i][j] is the min cost to repair first i robots using first j factories
    # Initialize with infinity
    inf = float('inf')
    dp = [[inf] * (m + 1) for _ in range(n + 1)]

    # Base case: 0 robots cost 0 to repair
    for j in range(m + 1):
        dp[0][j] = 0

    for j in range(1, m + 1):
        f_pos, f_limit = factory[j-1]
        for i in range(n + 1):
            # Option 1: Don't use this factory at all
            dp[i][j] = dp[i][j-1]

            # Option 2: Use this factory to repair k robots (1 <= k <= f_limit)
            cost = 0
            for k in range(1, min(i, f_limit) + 1):
                cost += abs(robot[i - k] - f_pos)
                if dp[i - k][j - 1] != inf:
                    dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + cost)

    return dp[n][m]
```
</details>
