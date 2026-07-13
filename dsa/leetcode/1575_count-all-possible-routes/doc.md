# Count All Possible Routes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1575 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-all-possible-routes](https://leetcode.com/problems/count-all-possible-routes/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-all-possible-routes/).

### Goal
Count routes that start at `start`, may visit cities repeatedly, and end at
`finish` without spending more than the available fuel.

### Function Contract
**Inputs**

- `locations`: city positions on a line.
- `start`: the starting city index.
- `finish`: the destination city index.
- `fuel`: the starting fuel amount.

**Return value**

The number of valid routes modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `locations = [2, 3, 6, 8, 4], start = 1, finish = 3, fuel = 5`
- Output: `4`

**Example 2**

- Input: `locations = [4, 3, 1], start = 1, finish = 0, fuel = 6`
- Output: `5`

**Example 3**

- Input: `locations = [5, 2, 1], start = 0, finish = 2, fuel = 3`
- Output: `0`

---

## Solution
### Approach
Use memoized dynamic programming on `(city, remaining_fuel)`. Each state counts
one route immediately if `city == finish`, then tries moving to every other city
whose distance cost fits in the remaining fuel.

### Complexity Analysis
- **Time Complexity**: `O(n^2 * fuel)`.
- **Space Complexity**: `O(n * fuel)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
from functools import lru_cache


def solve(locations, start, finish, fuel):
    mod = 10**9 + 7
    n = len(locations)
    if n == 0:
        return 0
    start %= n
    finish %= n
    fuel = max(0, fuel)

    @lru_cache(maxsize=None)
    def dp(city, remaining):
        total = 1 if city == finish else 0
        for nxt in range(n):
            if nxt == city:
                continue
            cost = abs(locations[city] - locations[nxt])
            if cost == 0:
                continue
            if cost <= remaining:
                total += dp(nxt, remaining - cost)
        return total % mod

    return dp(start, fuel)
```
</details>
