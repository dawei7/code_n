# Paint House IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3429 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [paint-house-iv](https://leetcode.com/problems/paint-house-iv/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/paint-house-iv/).

### Goal
You are tasked with painting a row of $n$ houses using $m$ available colors. The houses are arranged in a line, and you must paint them such that no two adjacent houses share the same color. Additionally, the first and last houses must also have different colors. Given a cost matrix where `cost[i][j]` represents the cost of painting house $i$ with color $j$, determine the minimum total cost to paint all houses while satisfying these constraints.

### Function Contract
**Inputs**

- `n`: An integer representing the number of houses (where $n$ is even).
- `cost`: A 2D list of integers of size $(n \times m)$, where `cost[i][j]` is the cost of painting house $i$ with color $j$.

**Return value**

- An integer representing the minimum cost to paint all houses, or -1 if it is impossible to satisfy the constraints.

### Examples
**Example 1**

- Input: `n = 4, cost = [[3,5,7],[6,2,9],[4,8,1],[7,3,5]]`
- Output: `12`

**Example 2**

- Input: `n = 2, cost = [[1,2,3],[2,3,4]]`
- Output: `4`

**Example 3**

- Input: `n = 4, cost = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]`
- Output: `24`

---

## Solution
### Approach
The problem is solved using Dynamic Programming. Since the constraints involve the first and last houses, we can observe that the houses can be paired from the outside in (house $i$ and house $n-1-i$). We define `dp[i][c1][c2]` as the minimum cost to paint the first $i$ pairs of houses (from the ends) such that the $i$-th house from the start has color `c1` and the $i$-th house from the end has color `c2`.

### Complexity Analysis
- **Time Complexity**: $O(n \cdot m^2)$, where $n$ is the number of houses and $m$ is the number of colors. We iterate through $n/2$ pairs, and for each pair, we transition between $m^2$ color combinations.
- **Space Complexity**: $O(m^2)$, as we only need the results from the previous pair to calculate the current pair.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n: int, cost: list[list[int]]) -> int:
    m = len(cost[0])
    # dp[c1][c2] stores the min cost for the current pair of houses
    # (i, n-1-i) having colors c1 and c2 respectively.
    dp = [[float('inf')] * m for _ in range(m)]

    # Base case: the outermost pair (0, n-1)
    for c1 in range(m):
        for c2 in range(m):
            if c1 != c2:
                dp[c1][c2] = cost[0][c1] + cost[n - 1][c2]

    # Iterate through the remaining n/2 - 1 pairs
    for i in range(1, n // 2):
        new_dp = [[float('inf')] * m for _ in range(m)]
        # Precompute min values to optimize transition from O(m^4) to O(m^2)
        # min_prev[prev_c1][prev_c2] is the min cost of previous pair
        # We need to find min(dp[prev_c1][prev_c2]) where prev_c1 != c1 and prev_c2 != c2

        # To optimize, find the smallest and second smallest values in dp
        # for each row and column, but given m is usually small,
        # a direct O(m^4) or O(m^3) is often acceptable.
        # Here we use O(m^3) by pre-calculating row/col minimums.

        for c1 in range(m):
            for c2 in range(m):
                if c1 == c2:
                    continue

                current_cost = cost[i][c1] + cost[n - 1 - i][c2]

                # Find min(dp[pc1][pc2]) where pc1 != c1 and pc2 != c2
                for pc1 in range(m):
                    if pc1 == c1: continue
                    for pc2 in range(m):
                        if pc2 == c2: continue
                        if dp[pc1][pc2] + current_cost < new_dp[c1][c2]:
                            new_dp[c1][c2] = dp[pc1][pc2] + current_cost
        dp = new_dp

    ans = min(min(row) for row in dp)
    return int(ans) if ans != float('inf') else -1
```
</details>
