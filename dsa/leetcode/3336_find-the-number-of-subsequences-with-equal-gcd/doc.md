# Find the Number of Subsequences With Equal GCD

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3336 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-number-of-subsequences-with-equal-gcd](https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/).

### Goal
Given an array of integers, determine the number of pairs of non-empty disjoint subsequences such that the greatest common divisor (GCD) of the elements in the first subsequence equals the GCD of the elements in the second subsequence. Since the result can be very large, return it modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.

**Return value**

- An integer representing the count of pairs of disjoint subsequences with equal GCD, modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `5`
- Explanation: The pairs of subsequences are ([1], [1]), ([2], [2]), ([3], [3]), ([1, 2], [1, 2]), ([1, 3], [1, 3]).

**Example 2**

- Input: `nums = [10, 20, 30]`
- Output: `2`
- Explanation: The pairs are ([10], [10]), ([20], [20]), ([30], [30]), ([10, 20], [10, 20]), ([10, 30], [10, 30]), ([20, 30], [20, 30]), ([10, 20, 30], [10, 20, 30]). (Note: GCDs must match).

**Example 3**

- Input: `nums = [1, 1, 1, 1]`
- Output: `65`

---

## Solution
### Approach
The problem is solved using Dynamic Programming with state compression. We maintain a DP table `dp[g1][g2]` representing the number of ways to form two disjoint subsequences with GCDs `g1` and `g2` respectively. For each number `x` in the input, we update the DP table by considering three choices: adding `x` to the first subsequence, adding `x` to the second, or ignoring `x`. We use the property that the GCD of a subsequence is always a divisor of the elements within it, limiting the state space to the maximum value in `nums` (up to 200).

### Complexity Analysis
- **Time Complexity**: `O(N * M^2)`, where `N` is the length of the array and `M` is the maximum value in the array (200).
- **Space Complexity**: `O(M^2)` to store the DP table.

### Reference Implementations
<details>
<summary>python</summary>

```python
import math


def solve(nums: list[int]) -> int:
    mod = 10**9 + 7
    max_value = max(nums)
    dp = [[0] * (max_value + 1) for _ in range(max_value + 1)]
    dp[0][0] = 1

    for value in nums:
        next_dp = [row[:] for row in dp]
        for g1 in range(max_value + 1):
            for g2 in range(max_value + 1):
                count = dp[g1][g2]
                if count == 0:
                    continue

                next_g1 = value if g1 == 0 else math.gcd(g1, value)
                next_g2 = value if g2 == 0 else math.gcd(g2, value)
                next_dp[next_g1][g2] = (next_dp[next_g1][g2] + count) % mod
                next_dp[g1][next_g2] = (next_dp[g1][next_g2] + count) % mod
        dp = next_dp

    return sum(dp[g][g] for g in range(1, max_value + 1)) % mod
```
</details>
