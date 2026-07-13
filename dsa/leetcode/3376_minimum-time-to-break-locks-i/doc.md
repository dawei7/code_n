# Minimum Time to Break Locks I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3376 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Breadth-First Search, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-time-to-break-locks-i](https://leetcode.com/problems/minimum-time-to-break-locks-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-time-to-break-locks-i/).

### Goal
You must break every lock in any order. Each lock has a required energy `strength[i]`. The sword starts with energy `0` and factor `x = 1`; every minute, energy increases by `x`. When the current energy reaches a lock's strength, that lock can be broken, energy resets to `0`, and `x` increases by `k`. Return the minimum number of minutes needed to break all locks.

### Function Contract
**Inputs**

- `locks`: A list of lock strengths.
- `k`: The amount added to the energy growth factor after each broken lock.

**Return value**

- An integer representing the minimum total time required to break all locks.

### Examples
**Example 1**

- Input: `locks = [3, 4, 1], k = 1`
- Output: `4`

**Example 2**

- Input: `locks = [2, 5, 4], k = 2`
- Output: `5`

**Example 3**

- Input: `locks = [6, 7], k = 3`
- Output: `4`

---

## Solution
### Approach
The problem can be solved using Bitmask Dynamic Programming or Backtracking with memoization. Since the number of locks is small (implied by the constraints of "I" version), we can represent the set of broken locks as a bitmask. The state is defined by `(mask, current_factor)`, where `mask` tracks which locks are broken and `current_factor` is the current multiplier.

### Complexity Analysis
- **Time Complexity**: `O(n * 2^n)`, where `n` is the number of locks. We explore all permutations of locks, and the state space is defined by the bitmask of broken locks.
- **Space Complexity**: `O(2^n)` to store the memoization table for the visited states.

### Reference Implementations
<details>
<summary>python</summary>

```python
import functools
import math


def solve(locks: list[int], k: int) -> int:
    n = len(locks)

    @functools.lru_cache(None)
    def dp(mask: int) -> int:
        broken = mask.bit_count()
        if broken == n:
            return 0

        factor = 1 + broken * k
        best = math.inf

        for index, strength in enumerate(locks):
            if mask & (1 << index):
                continue
            minutes = math.ceil(strength / factor)
            best = min(best, minutes + dp(mask | (1 << index)))

        return best

    return dp(0)
```
</details>
