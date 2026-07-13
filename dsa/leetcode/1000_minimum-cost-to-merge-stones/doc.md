# Minimum Cost to Merge Stones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1000 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-cost-to-merge-stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-cost-to-merge-stones/).

### Goal
Given stone piles in a row, each operation may merge exactly `k` consecutive piles into one pile whose weight is their sum. Return the minimum total merge cost needed to end with one pile, or `-1` if the merge count can never reach one pile.

### Function Contract
**Inputs**

- `stones`: List[int] pile weights
- `k`: int number of adjacent piles merged per operation

**Return value**

int - minimum total cost, or `-1` if impossible

### Examples
**Example 1**

- Input: `stones = [3, 2, 4, 1], k = 2`
- Output: `20`

**Example 2**

- Input: `stones = [3, 2, 4, 1], k = 3`
- Output: `-1`

**Example 3**

- Input: `stones = [3, 5, 1, 2, 6], k = 3`
- Output: `25`

---

## Solution
### Approach
Interval dynamic programming with prefix sums.

### Complexity Analysis
- **Time Complexity**: `O(n^3 / k)` in the direct interval DP form
- **Space Complexity**: `O(n^2)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1000: Minimum Cost to Merge Stones."""


def solve(stones: list[int], k: int) -> int:
    n = len(stones)
    if (n - 1) % (k - 1) != 0:
        return -1

    prefix = [0]
    for value in stones:
        prefix.append(prefix[-1] + value)

    dp = [[0] * n for _ in range(n)]
    for length in range(k, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            best = min(
                dp[left][mid] + dp[mid + 1][right]
                for mid in range(left, right, k - 1)
            )
            if (length - 1) % (k - 1) == 0:
                best += prefix[right + 1] - prefix[left]
            dp[left][right] = best
    return dp[0][n - 1]
```
</details>
