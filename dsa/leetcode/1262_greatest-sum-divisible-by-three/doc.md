# Greatest Sum Divisible by Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1262 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [greatest-sum-divisible-by-three](https://leetcode.com/problems/greatest-sum-divisible-by-three/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/greatest-sum-divisible-by-three/).

### Goal
Choose a subsequence of numbers with the largest possible sum that is divisible by `3`.

### Function Contract
**Inputs**

- `nums`: positive integer array.

**Return value**

The greatest sum divisible by `3`.

### Examples
**Example 1**

- Input: `nums = [3,6,5,1,8]`
- Output: `18`

**Example 2**

- Input: `nums = [4]`
- Output: `0`

**Example 3**

- Input: `nums = [1,2,3,4,4]`
- Output: `12`

---

## Solution
### Approach
Dynamic programming by remainder.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums):
    dp = [0, float("-inf"), float("-inf")]
    for value in nums:
        current = dp[:]
        for residue in range(3):
            current[(residue + value) % 3] = max(current[(residue + value) % 3], dp[residue] + value)
        dp = current
    return dp[0]
```
</details>
