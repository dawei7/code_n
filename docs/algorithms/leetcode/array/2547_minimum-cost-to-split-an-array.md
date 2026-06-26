# Minimum Cost to Split an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2547 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Dynamic Programming, Counting |
| Official Link | [minimum-cost-to-split-an-array](https://leetcode.com/problems/minimum-cost-to-split-an-array/) |

## Problem Description & Examples
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

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming. We define `dp[i]` as the minimum cost to partition the prefix `nums[0...i-1]`. To compute `dp[i]`, we iterate through all possible split points `j < i`, calculating the cost of the subarray `nums[j...i-1]` and adding it to `dp[j]`. To efficiently calculate the "trimming cost" (number of elements appearing > 1 time) for every subarray, we precompute these values or update them incrementally as we iterate backwards from `i-1` to `0`.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`, where `n` is the length of the array. We have a nested loop structure where the outer loop iterates through the array and the inner loop calculates subarray costs.
- **Space Complexity**: `O(n)` to store the DP table and the frequency map used during the inner loop calculation.
