# Find the Maximum Length of a Good Subsequence I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3176 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Dynamic Programming |
| Official Link | [find-the-maximum-length-of-a-good-subsequence-i](https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/) |

## Problem Description & Examples
### Goal
Given an integer array `nums` and an integer `k`, determine the length of the longest subsequence such that the number of adjacent pairs with different values in the subsequence does not exceed `k`.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the maximum allowed count of adjacent elements that are not equal.

**Return value**

- An integer representing the maximum length of the valid subsequence.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1, 1, 3], k = 2`
- Output: `4`

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5, 1], k = 0`
- Output: `2`

**Example 3**

- Input: `nums = [1, 2, 1, 2, 1, 2], k = 1`
- Output: `3`

---

## Underlying Base Algorithm(s)
Dynamic Programming. Specifically, we maintain a DP table `dp[v][i]` representing the maximum length of a subsequence ending with value `v` having exactly `i` adjacent unequal pairs. Transitions involve iterating through previous values and updating the state based on whether the current element matches the previous one.

---

## Complexity Analysis
- **Time Complexity**: `O(n * k)`, where `n` is the length of the input array and `k` is the allowed number of unequal adjacent pairs.
- **Space Complexity**: `O(n * k)` in the worst case, though it can be optimized to `O(unique_elements * k)`.
