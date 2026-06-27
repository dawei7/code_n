# Minimum Cost to Divide Array Into Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3500 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Prefix Sum |
| Official Link | [minimum-cost-to-divide-array-into-subarrays](https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/) |

## Problem Description & Examples
### Goal
Given an integer array `nums` and an integer `k`, partition the array into exactly `k` non-empty contiguous subarrays such that the sum of the costs of these subarrays is minimized. The cost of a subarray is defined as the sum of its first element and its last element.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the array to be partitioned.
- `k`: An integer representing the exact number of subarrays required.

**Return value**

- An integer representing the minimum total cost of the partition.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1, 2, 1], k = 3`
- Output: `6`
- Explanation: Partition into `[1, 2], [1, 2], [1]` (costs: 1+2, 1+2, 1+1 = 3+3+2 = 8) or `[1], [2, 1], [2, 1]` (costs: 1+1, 2+1, 2+1 = 2+3+3 = 8). Wait, the optimal is `[1, 2, 1], [2], [1]`? No, the cost is `nums[0] + nums[last]`. For `[1, 2, 1]`, cost is `1+1=2`. For `[2]`, cost is `2+2=4`. For `[1]`, cost is `1+1=2`. Total = 8. Actually, for `[1], [2, 1, 2], [1]`, cost is `1+1 + 2+2 + 1+1 = 8`.

**Example 2**

- Input: `nums = [1, 3, 1], k = 2`
- Output: `5`
- Explanation: Partition into `[1, 3]` and `[1]`. Cost: `(1+3) + (1+1) = 4 + 2 = 6`. Or `[1]` and `[3, 1]`. Cost: `(1+1) + (3+1) = 2 + 4 = 6`.

**Example 3**

- Input: `nums = [5, 4, 3], k = 3`
- Output: `18`
- Explanation: Each element must be its own subarray. Cost: `(5+5) + (4+4) + (3+3) = 10 + 8 + 6 = 24`.

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming. Let `dp[i][j]` be the minimum cost to partition the prefix `nums[0...i]` into `j` subarrays. The transition involves iterating over the possible split points for the last subarray. Given the constraints, we optimize the state space and transition using the observation that the first element of the first subarray is always `nums[0]`.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2 * k)` where `n` is the length of the array. This can be optimized to `O(n^2)` if `k` is treated as a constant or via space-optimized DP.
- **Space Complexity**: `O(n * k)` to store the DP table, which can be reduced to `O(n)` using two rows.
