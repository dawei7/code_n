# Find the Sum of the Power of All Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3082 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-sum-of-the-power-of-all-subsequences](https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/).

### Goal
Given an array of integers `nums` and an integer `k`, calculate the sum of the "power" of all possible subsequences of `nums`. The power of a subsequence is defined as the number of its own subsequences that sum up to exactly `k`. Since the result can be very large, return it modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
- `k`: An integer representing the target sum.

**Return value**

- An integer representing the total sum of powers of all subsequences, modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3], k = 3`
- Output: `6`

**Example 2**

- Input: `nums = [1, 2, 3], k = 7`
- Output: `0`

**Example 3**

- Input: `nums = [8, 2, 7], k = 5`
- Output: `4`

---

## Solution
### Approach
The problem is solved using Dynamic Programming. We define `dp[i][j]` as the number of subsequences of the input array that sum to `j` using a subset of the first `i` elements. To calculate the total power, we observe that if a subsequence of length `L` has `count` sub-subsequences that sum to `k`, then for every element not in that subsequence, we have two choices: include it or exclude it. This effectively multiplies the count by `2^(n - L)`. By iterating through all possible sums `j` and subsequence lengths `L`, we aggregate the contributions.

### Complexity Analysis
- **Time Complexity**: `O(n * k)`, where `n` is the length of the array and `k` is the target sum. We iterate through the array and update the DP table for each possible sum up to `k`.
- **Space Complexity**: `O(n * k)` (can be optimized to `O(k)`), where we store the number of ways to achieve a sum `j` using a specific number of elements.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    mod = 10**9 + 7
    dp = [0] * (k + 1)
    dp[0] = 1

    for value in nums:
        nxt = [(count * 2) % mod for count in dp]
        if value <= k:
            for total in range(value, k + 1):
                nxt[total] = (nxt[total] + dp[total - value]) % mod
        dp = nxt

    return dp[k]
```
</details>
