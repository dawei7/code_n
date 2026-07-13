# Stone Game II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1140 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Prefix Sum, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [stone-game-ii](https://leetcode.com/problems/stone-game-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/stone-game-ii/).

### Goal
Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, each pile having a positive integer number of stones `piles[i]`.

Alice and Bob take turns, with Alice starting first. Initially, `M = 1`. On each player's turn, that player can take all the stones in the first `X` remaining piles, where `1 <= X <= 2M`. Then, we set `M = max(M, X)`.

The game continues until all the stones have been taken. Return the maximum number of stones Alice can get.

### Function Contract
**Inputs**

- `piles`: List[int]

**Return value**

int - maximum stones Alice can get

### Examples
**Example 1**

- Input: `piles = [2, 7, 9, 4, 4]`
- Output: `10`

**Example 2**

- Input: `piles = [14, 2, 9]`
- Output: `16`

**Example 3**

- Input: `piles = [19, 3]`
- Output: `22`

---

## Solution
### Approach
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

### Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
<details>
<summary>python</summary>

```python
from functools import lru_cache


def solve(piles):
    n = len(piles)
    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] + piles[i]

    @lru_cache(None)
    def dp(i, m):
        if i + 2 * m >= n:
            return suffix[i]
        best_opponent = float("inf")
        for x in range(1, 2 * m + 1):
            best_opponent = min(best_opponent, dp(i + x, max(m, x)))
        return suffix[i] - best_opponent

    return dp(0, 1)
```
</details>
