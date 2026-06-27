# Sum of Good Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3351 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Dynamic Programming |
| Official Link | [sum-of-good-subsequences](https://leetcode.com/problems/sum-of-good-subsequences/) |

## Problem Description & Examples
### Goal
Given an array of integers, a subsequence is considered "good" if the absolute difference between any two adjacent elements in the subsequence is exactly 1. Calculate the sum of all good subsequences. Since the result can be very large, return it modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 <= nums.length <= 10^5 and 1 <= nums[i] <= 10^6.

**Return value**

- An integer representing the sum of all good subsequences modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1]`
- Output: `14`
- Explanation: The good subsequences are [1], [2], [1], [1, 2], [2, 1], [1, 1] (invalid), [1, 2, 1]. Summing their values: 1+2+1+3+3+4 = 14.

**Example 2**

- Input: `nums = [3, 4, 5]`
- Output: `40`

**Example 3**

- Input: `nums = [1, 1]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Dynamic Programming with Hash Maps. We maintain two states for each unique value `x` encountered: `count[x]` (the number of good subsequences ending with `x`) and `total_sum[x]` (the sum of all good subsequences ending with `x`). For each element `v` in the input, we update these states based on the values `v-1` and `v+1`.

---

## Complexity Analysis
- **Time Complexity**: O(N), where N is the length of the input array, as we iterate through the array once and perform constant-time hash map lookups.
- **Space Complexity**: O(U), where U is the number of unique elements in the input array, used to store the DP states in hash maps.
