# Minimum Cost to Split an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2547 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-cost-to-split-an-array](https://leetcode.com/problems/minimum-cost-to-split-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-cost-to-split-an-array/).

### Goal
The objective is to partition an array of integers into one or more contiguous subarrays such that the total cost of the partition is minimized. The cost of a single subarray is defined as `k` plus the number of elements in that subarray that appear more than once within that specific subarray. The total cost is the sum of the costs of all resulting subarrays.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the sequence to be partitioned.
- `k`: An integer representing the base cost added to every subarray partition.

**Return value**

- An integer representing the minimum possible total cost to partition the entire array.

### Examples
**Example 1**

- Input: `nums = [1,2,1,2,1,3,3], k = 2`
- Output: `8`

**Example 2**

- Input: `nums = [1,2,1,2,1], k = 2`
- Output: `6`

**Example 3**

- Input: `nums = [1,2,1,2,1], k = 5`
- Output: `10`

---

## Solution
### Approach
The problem is solved using Dynamic Programming. We define `dp[i]` as the minimum cost to partition the prefix `nums[0...i-1]`. To compute `dp[i]`, we iterate through all possible split points `j < i`, calculating the cost of the subarray `nums[j...i-1]` and adding it to `dp[j]`. To efficiently calculate the "trimming cost" (number of elements appearing > 1 time) for every subarray, we precompute these values or update them incrementally as we iterate backwards from `i-1` to `0`.

### Complexity Analysis
- **Time Complexity**: `O(n^2)`, where `n` is the length of the array. We have a nested loop structure where the outer loop iterates through the array and the inner loop calculates subarray costs.
- **Space Complexity**: `O(n)` to store the DP table and the frequency map used during the inner loop calculation.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    # dp[i] will store the minimum cost to partition nums[0...i-1]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    # Precompute trimming costs for all subarrays [j, i-1]
    # cost[j][i] = number of elements that appear more than once in nums[j...i]
    # Since we need this for DP, we can compute it on the fly.

    for i in range(1, n + 1):
        freq = {}
        trimming_cost = 0
        # Iterate backwards to build the subarray nums[j...i-1]
        for j in range(i - 1, -1, -1):
            val = nums[j]
            freq[val] = freq.get(val, 0) + 1

            if freq[val] == 2:
                # This element now contributes to the trimming cost
                trimming_cost += 2
            elif freq[val] > 2:
                # This element was already contributing, now it adds 1 more
                trimming_cost += 1

            current_subarray_cost = k + trimming_cost
            if dp[j] + current_subarray_cost < dp[i]:
                dp[i] = dp[j] + current_subarray_cost

    return int(dp[n])
```
</details>
