# Find the Maximum Length of Valid Subsequence II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3202 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [find-the-maximum-length-of-valid-subsequence-ii](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/) |

## Problem Description & Examples
### Goal
Given an integer array `nums` and an integer `k`, determine the length of the longest subsequence such that the sum of every two adjacent elements in the subsequence is divisible by `k`.

### Function Contract
**Inputs**

- `nums`: A list of integers.
- `k`: An integer representing the divisor.

**Return value**

- An integer representing the maximum length of the valid subsequence.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4, 5], k = 2`
- Output: `3`
- Explanation: The subsequence `[1, 3, 5]` has adjacent sums `1+3=4` and `3+5=8`, both divisible by 2.

**Example 2**

- Input: `nums = [1, 4, 2, 3, 1, 4], k = 3`
- Output: `3`
- Explanation: The subsequence `[1, 2, 1]` has adjacent sums `1+2=3` and `2+1=3`, both divisible by 3.

**Example 3**

- Input: `nums = [7, 1, 1, 7, 1], k = 3`
- Output: `4`
- Explanation: The subsequence `[7, 1, 7, 1]` has adjacent sums divisible by 3.

---

## Underlying Base Algorithm(s)
Dynamic Programming. Specifically, we track the state `dp[remainder_a][remainder_b]`, which represents the length of the longest valid subsequence ending with a value having remainder `remainder_b` when the previous element had remainder `remainder_a`. Since we only care about the remainder modulo `k`, we can reduce the state space to `k x k`.

---

## Complexity Analysis
- **Time Complexity**: `O(n * k)`, where `n` is the length of the array. We iterate through the array once and for each element, we perform constant time updates for all possible remainders.
- **Space Complexity**: `O(k^2)`, as we maintain a 2D table of size `k` by `k` to store the lengths of subsequences ending in specific remainders.
