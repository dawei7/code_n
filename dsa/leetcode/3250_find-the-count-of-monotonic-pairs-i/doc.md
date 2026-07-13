# Find the Count of Monotonic Pairs I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3250 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Combinatorics, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-count-of-monotonic-pairs-i](https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/).

### Goal
Given an array of non-negative integers `nums`, determine the number of pairs of arrays `(arr1, arr2)` such that `arr1` is non-decreasing, `arr2` is non-increasing, and for every index `i`, `arr1[i] + arr2[i] == nums[i]`. The result should be returned modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers.

**Return value**

- An integer representing the total count of valid pairs `(arr1, arr2)` modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [2, 3, 2]`
- Output: `4`

**Example 2**

- Input: `nums = [5, 5, 5, 5]`
- Output: `126`

**Example 3**

- Input: `nums = [1]`
- Output: `2`

---

## Solution
### Approach
The problem is solved using Dynamic Programming. Let `dp[i][v]` be the number of ways to choose `arr1[i] = v` such that the conditions are satisfied up to index `i`. Since `arr1[i] + arr2[i] = nums[i]`, choosing `arr1[i]` automatically determines `arr2[i]`. The constraints are `arr1[i] >= arr1[i-1]` and `arr2[i] <= arr2[i-1]`. Substituting `arr2`, the second condition becomes `nums[i] - v <= nums[i-1] - arr1[i-1]`, or `arr1[i-1] <= v - (nums[i] - nums[i-1])`. We optimize the transition using prefix sums to achieve O(n * max(nums)) time complexity.

### Complexity Analysis
- **Time Complexity**: `O(n * m)`, where `n` is the length of `nums` and `m` is the maximum value in `nums`.
- **Space Complexity**: `O(m)` using space-optimized DP arrays.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    max_val = max(nums)

    # dp[v] stores the number of ways to have arr1[i] = v
    # Initialize for i = 0: arr1[0] can be any value from 0 to nums[0]
    dp = [1] * (max_val + 1)
    for v in range(max_val + 1):
        if v > nums[0]:
            dp[v] = 0

    for i in range(1, n):
        new_dp = [0] * (max_val + 1)
        # Prefix sums of the previous dp state to optimize transition
        prefix_sum = [0] * (max_val + 2)
        for v in range(max_val + 1):
            prefix_sum[v + 1] = (prefix_sum[v] + dp[v]) % MOD

        for v in range(nums[i] + 1):
            # Conditions:
            # 1. arr1[i-1] <= v
            # 2. arr2[i-1] >= arr2[i] => nums[i-1] - arr1[i-1] >= nums[i] - v
            #    => arr1[i-1] <= v - (nums[i] - nums[i-1])
            # So, arr1[i-1] <= min(v, v - nums[i] + nums[i-1])

            upper = min(v, v - nums[i] + nums[i-1])
            if upper >= 0:
                # Sum of dp[0...upper]
                limit = min(upper, nums[i-1])
                new_dp[v] = prefix_sum[limit + 1]
        dp = new_dp

    return sum(dp) % MOD
```
</details>
