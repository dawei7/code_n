# Number of Great Partitions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2518 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-great-partitions](https://leetcode.com/problems/number-of-great-partitions/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-great-partitions/).

### Goal
Given an array of integers and an integer `k`, determine the number of ways to partition the array into two non-empty subsets such that the sum of elements in each subset is at least `k`. Since the result can be very large, return it modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the elements to be partitioned.
- `k`: An integer representing the minimum sum threshold for each subset.

**Return value**

- An integer representing the total count of valid partitions modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4], k = 4`
- Output: `6`

**Example 2**

- Input: `nums = [3,3,3], k = 4`
- Output: `0`

**Example 3**

- Input: `nums = [6,6], k = 2`
- Output: `2`

---

## Solution
### Approach
The problem is solved using the Principle of Inclusion-Exclusion combined with 0/1 Knapsack Dynamic Programming.
1. Total ways to partition a set into two subsets is 2^n.
2. A partition is "bad" if at least one subset has a sum strictly less than `k`.
3. We calculate the number of subsets with sum `s < k` using DP.
4. The final answer is (Total - 2 * (subsets with sum < k)) % MOD, accounting for the fact that both subsets must be non-empty and satisfy the condition.

### Complexity Analysis
- **Time Complexity**: O(n * k), where n is the length of the array and k is the threshold. We iterate through the array and update a DP table of size k.
- **Space Complexity**: O(k), as we only need the current and previous states of the DP table to calculate the number of subsets with a specific sum.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    total_sum = sum(nums)

    # If the total sum is less than 2*k, no partition can satisfy the condition
    if total_sum < 2 * k:
        return 0

    # dp[i] will store the number of subsets that sum up to i
    dp = [0] * k
    dp[0] = 1

    for x in nums:
        for j in range(k - 1, x - 1, -1):
            dp[j] = (dp[j] + dp[j - x]) % MOD

    # The number of subsets with sum < k
    bad_subsets_count = sum(dp) % MOD

    # Total ways to form subsets is 2^n.
    # A partition is invalid if one subset has sum < k.
    # Since total_sum >= 2*k, it's impossible for both subsets to be < k.
    # Thus, we subtract 2 * bad_subsets_count from 2^n.
    # We also exclude the empty set and the full set cases if necessary,
    # but the problem implies non-empty subsets.

    total_ways = pow(2, n, MOD)
    # Subtract the cases where one subset is < k (multiplied by 2 for both sides)
    ans = (total_ways - 2 * bad_subsets_count) % MOD

    return ans
```
</details>
