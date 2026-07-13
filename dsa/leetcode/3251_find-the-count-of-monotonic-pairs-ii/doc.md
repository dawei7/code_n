# Find the Count of Monotonic Pairs II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3251 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Combinatorics, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-count-of-monotonic-pairs-ii](https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/).

### Goal
Given an array of non-negative integers `nums`, determine the number of pairs of arrays `(arr1, arr2)` such that `arr1` is non-decreasing, `arr2` is non-increasing, and for every index `i`, `arr1[i] + arr2[i] == nums[i]`. The result should be returned modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers where `0 <= nums[i] <= 1000`.

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
The problem is solved using Dynamic Programming optimized with Prefix Sums. Let `dp[i][j]` be the number of ways to choose `arr1[i] = j`. The constraints `arr1[i] >= arr1[i-1]` and `arr2[i] <= arr2[i-1]` (which implies `nums[i] - arr1[i] <= nums[i-1] - arr1[i-1]`) lead to the condition `arr1[i-1] <= min(j, j - (nums[i] - nums[i-1]))`. By maintaining a prefix sum of the previous DP row, we can calculate the transition in O(1) time, reducing the overall complexity from O(N * max(nums)^2) to O(N * max(nums)).

### Complexity Analysis
- **Time Complexity**: O(N * M), where N is the length of `nums` and M is the maximum value in `nums`.
- **Space Complexity**: O(M), as we only need the current and previous rows of the DP table.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    max_val = max(nums)

    # dp[j] stores the number of ways to have arr1[i] = j
    # Initially for i = 0, arr1[0] can be any value from 0 to nums[0]
    dp = [1] * (max_val + 1)

    for i in range(1, n):
        new_dp = [0] * (max_val + 1)
        prefix_sum = [0] * (max_val + 2)

        # Build prefix sum of the previous dp state
        for j in range(max_val + 1):
            prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % MOD

        for j in range(nums[i] + 1):
            # arr1[i-1] <= j
            # arr2[i] <= arr2[i-1] => nums[i]-j <= nums[i-1]-arr1[i-1]
            # => arr1[i-1] <= nums[i-1] - nums[i] + j
            upper = min(j, nums[i-1] - nums[i] + j)

            if upper >= 0:
                # Sum of dp[0...upper]
                limit = min(upper, nums[i-1])
                new_dp[j] = prefix_sum[limit + 1]

        dp = new_dp

    return sum(dp) % MOD
```
</details>
