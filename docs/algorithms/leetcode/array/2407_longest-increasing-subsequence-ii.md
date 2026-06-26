# Longest Increasing Subsequence II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2407 |
| Difficulty | Hard |
| Topics | Array, Divide and Conquer, Dynamic Programming, Binary Indexed Tree, Segment Tree, Queue, Monotonic Queue |
| Official Link | [longest-increasing-subsequence-ii](https://leetcode.com/problems/longest-increasing-subsequence-ii/) |

## Problem Description & Examples
### Goal
Given an integer array `nums` and an integer `k`, find the length of the longest subsequence such that for any two consecutive elements in the subsequence, their absolute difference is at most `k`. Specifically, if the subsequence is `s[0], s[1], ..., s[m]`, then `s[i+1] - s[i] <= k` and `s[i+1] > s[i]` must hold for all valid `i`.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input sequence.
- `k`: An integer representing the maximum allowed difference between consecutive elements.

**Return value**

- An integer representing the length of the longest subsequence satisfying the condition.

### Examples
**Example 1**

- Input: `nums = [4,2,1,4,3,4,5,8,15], k = 3`
- Output: `5`

**Example 2**

- Input: `nums = [7,4,5,1,8,12,4,7], k = 5`
- Output: `4`

**Example 3**

- Input: `nums = [1,5], k = 1`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem is solved using a Segment Tree. Since we need to find the maximum length of a subsequence ending at a value `v` such that the previous value was in the range `[v-k, v-1]`, we can treat the values in `nums` as indices in a Segment Tree. The Segment Tree stores the maximum subsequence length found so far for each value. For each number `x` in `nums`, we query the range `[max(1, x-k), x-1]` to find the maximum length, then update the position `x` in the tree with `max_length + 1`.

---

## Complexity Analysis
- **Time Complexity**: `O(n log M)`, where `n` is the length of `nums` and `M` is the maximum value in `nums` (the range of the segment tree).
- **Space Complexity**: `O(M)`, required to store the segment tree nodes.
