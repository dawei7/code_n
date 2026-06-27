# Find the Maximum Length of a Good Subsequence II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3177 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Dynamic Programming |
| Official Link | [find-the-maximum-length-of-a-good-subsequence-ii](https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/) |

## Problem Description & Examples
### Goal
Given an integer array `nums` and an integer `k`, determine the length of the longest subsequence such that the number of adjacent pairs with different values in the subsequence does not exceed `k`.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the maximum allowed count of index-adjacent elements that are not equal.

**Return value**

- An integer representing the maximum length of the "good" subsequence.

### Examples
**Example 1**

- Input: `nums = [1,2,1,1,3], k = 2`
- Output: `4`

**Example 2**

- Input: `nums = [1,2,3,4,5,1], k = 0`
- Output: `2`

**Example 3**

- Input: `nums = [1,1,1,1], k = 0`
- Output: `4`

---

## Underlying Base Algorithm(s)
The problem is solved using Dynamic Programming with state optimization. Let `dp[v][i]` be the maximum length of a good subsequence ending with value `v` having exactly `i` "mismatches" (adjacent unequal elements). To optimize, we maintain `max_len[i]` (the global maximum length for `i` mismatches) and `best_with_val[v][i]` (the max length ending in `v` with `i` mismatches). By tracking the top two values for each `i`, we can update the DP state in $O(n \cdot k)$ time.

---

## Complexity Analysis
- **Time Complexity**: $O(n \cdot k)$, where $n$ is the length of the input array and $k$ is the allowed mismatch count.
- **Space Complexity**: $O(n \cdot k)$ in the worst case for the DP table, though it can be optimized to $O(k \cdot \text{distinct elements})$.
