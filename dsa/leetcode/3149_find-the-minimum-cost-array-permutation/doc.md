# Find the Minimum Cost Array Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3149 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-minimum-cost-array-permutation](https://leetcode.com/problems/find-the-minimum-cost-array-permutation/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-minimum-cost-array-permutation/).

### Goal
Given an array `nums` of length `n`, find a permutation `p` of the indices `[0, 1, ..., n-1]` such that the total cost, defined as the sum of `|nums[p[i]] - p[i+1]|` for `0 <= i < n-1` plus the final wrap-around cost `|nums[p[n-1]] - p[0]|`, is minimized. If multiple permutations yield the same minimum cost, return the lexicographically smallest permutation.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the values at each index.

**Return value**

- A list of integers representing the permutation of indices `[0, 1, ..., n-1]` that achieves the minimum cost.

### Examples
**Example 1**

- Input: `nums = [1, 0, 2]`
- Output: `[0, 1, 2]`
- Explanation: The cost is `|nums[0]-1| + |nums[1]-2| + |nums[2]-0| = |1-1| + |0-2| + |2-0| = 0 + 2 + 2 = 4`.

**Example 2**

- Input: `nums = [0, 2, 1]`
- Output: `[0, 2, 1]`
- Explanation: The cost is `|nums[0]-2| + |nums[2]-1| + |nums[1]-0| = |0-2| + |1-1| + |2-0| = 2 + 0 + 2 = 4`.

**Example 3**

- Input: `nums = [1, 3, 2, 4]`
- Output: `[0, 2, 1, 3]`

---

## Solution
### Approach
The problem is a variation of the Traveling Salesperson Problem (TSP). Since `n` is small (up to 14), we use Dynamic Programming with Bitmasking. The state is defined by `(mask, last_index)`, representing the set of visited indices and the index visited most recently. We reconstruct the path by storing parent pointers or re-calculating the optimal transition.

### Complexity Analysis
- **Time Complexity**: `O(n^2 * 2^n)`, where `n` is the length of the array. We have `n * 2^n` states, and each state takes `O(n)` to compute.
- **Space Complexity**: `O(n * 2^n)` to store the DP table and the path reconstruction table.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> list[int]:
    from functools import lru_cache

    n = len(nums)
    full_mask = (1 << n) - 1

    @lru_cache(None)
    def best(mask: int, last: int) -> int:
        if mask == full_mask:
            return abs(nums[last] - 0)

        answer = float("inf")
        for nxt in range(n):
            if mask & (1 << nxt):
                continue
            answer = min(answer, abs(nums[last] - nxt) + best(mask | (1 << nxt), nxt))
        return int(answer)

    result = [0]
    mask = 1
    last = 0
    while mask != full_mask:
        target = best(mask, last)
        for nxt in range(n):
            if mask & (1 << nxt):
                continue
            if abs(nums[last] - nxt) + best(mask | (1 << nxt), nxt) == target:
                result.append(nxt)
                mask |= 1 << nxt
                last = nxt
                break

    return result
```
</details>
