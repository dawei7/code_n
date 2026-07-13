# Allocate Mailboxes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1478 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [allocate-mailboxes](https://leetcode.com/problems/allocate-mailboxes/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/allocate-mailboxes/).

### Goal
Place `k` mailboxes among houses on a line so the sum of distances from each house to its nearest mailbox is minimized.

### Function Contract
**Inputs**

- `houses`: house positions.
- `k`: number of mailboxes.

**Return value**

The minimum possible total distance.

### Examples
**Example 1**

- Input: `houses = [1,4,8,10,20], k = 3`
- Output: `5`

**Example 2**

- Input: `houses = [2,3,5,12,18], k = 2`
- Output: `9`

**Example 3**

- Input: `houses = [7,4,6,1], k = 1`
- Output: `8`

---

## Solution
### Approach
Sort positions, precompute the optimal one-mailbox cost for every interval using the median, then run DP over the first `i` houses and number of mailboxes used.

### Complexity Analysis
- **Time Complexity**: `O(n^2 k)`
- **Space Complexity**: `O(n^2 + nk)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(houses, k):
    houses = sorted(houses)
    n = len(houses)
    if n == 0:
        return 0
    k = max(1, min(int(k), n))
    cost = [[0] * n for _ in range(n)]
    for left in range(n):
        for right in range(left, n):
            mid = (left + right) // 2
            cost[left][right] = sum(abs(houses[i] - houses[mid]) for i in range(left, right + 1))
    inf = 10**18
    dp = [[inf] * n for _ in range(k + 1)]
    for i in range(n):
        dp[1][i] = cost[0][i]
    for boxes in range(2, k + 1):
        for i in range(n):
            for prev in range(i):
                dp[boxes][i] = min(dp[boxes][i], dp[boxes - 1][prev] + cost[prev + 1][i])
    return dp[k][n - 1]
```
</details>
