# Longest Subsequence With Decreasing Adjacent Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3409 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [longest-subsequence-with-decreasing-adjacent-difference](https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/) |

## Problem Description & Examples
### Goal
Given an array of integers, find the length of the longest subsequence such that the absolute difference between every pair of adjacent elements in the subsequence is strictly decreasing. Specifically, if the subsequence is $s_1, s_2, \dots, s_k$, then $|s_1 - s_2| > |s_2 - s_3| > \dots > |s_{k-1} - s_k|$.

### Function Contract
**Inputs**

- `nums`: A list of integers where $1 \le \text{nums}[i] \le 300$.

**Return value**

- An integer representing the maximum length of a valid subsequence.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `4`
- Explanation: The subsequence `[1, 2, 3, 4]` has differences `|1-2|=1`, `|2-3|=1`, `|3-4|=1`. Wait, the condition is strictly decreasing. For `[1, 2, 3, 4]`, differences are `1, 1, 1` (not strictly decreasing). A valid one is `[1, 4, 2, 3]` with differences `3, 2, 1`.

**Example 2**

- Input: `nums = [8, 6, 6, 2]`
- Output: `4`
- Explanation: Subsequence `[8, 6, 2]` has differences `2, 4` (not decreasing). Subsequence `[8, 2, 6]` has differences `6, 4`.

**Example 3**

- Input: `nums = [1, 1, 1, 1]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Dynamic Programming. We maintain a 2D DP table `dp[last_val][diff]`, representing the length of the longest valid subsequence ending with value `last_val` where the *previous* adjacent difference was `diff`. Since the values are bounded by 300, we can iterate through the array and update the state based on the transition: `dp[current_val][new_diff] = max(dp[prev_val][old_diff] + 1)` for all `old_diff > new_diff`.

---

## Complexity Analysis
- **Time Complexity**: $O(n \cdot M^2)$, where $n$ is the length of the array and $M$ is the maximum value in the array (300).
- **Space Complexity**: $O(M^2)$ to store the DP table.
