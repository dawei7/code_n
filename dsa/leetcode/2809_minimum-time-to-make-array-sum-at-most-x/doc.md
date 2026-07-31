# Minimum Time to Make Array Sum At Most x

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2809 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/) |

## Problem Description

### Goal

You are given equal-length 0-indexed arrays `nums1` and `nums2`. At the beginning of every second, each `nums1[i]` increases by `nums2[i]`. After all increments occur, you may choose one index and reset its current `nums1` value to zero. The choice can differ from second to second.

Given a limit `x`, return the minimum number of seconds after which the sum of `nums1` can be at most `x`. The sum may already satisfy the limit at time zero. If no sequence of resets can ever achieve the required sum, return `-1`. All increments in a second happen before its optional reset.

### Function Contract

**Inputs**

- `nums1`: A list of $n$ positive initial values, each at most $10^3$.
- `nums2`: A list of $n$ nonnegative per-second increments, each at most $10^3$.
- `x`: The target upper bound, where $0 \leq x \leq 10^6$.

The arrays have equal length and $1 \leq n \leq 10^3$.

**Return value**

Return the minimum feasible number of seconds, or `-1` when the sum cannot be reduced to at most `x`.

### Examples

**Example 1**

- Input: `nums1 = [1, 2, 3]`, `nums2 = [1, 2, 3]`, `x = 4`
- Output: `3`
- Explanation: Resetting indices in increasing increment order leaves `[2, 2, 0]` after three seconds, whose sum is $4$.

**Example 2**

- Input: `nums1 = [1, 2, 3]`, `nums2 = [3, 3, 3]`, `x = 4`
- Output: `-1`
- Explanation: Even the best reset sequence cannot offset the total growth enough to reach the limit.

**Example 3**

- Input: `nums1 = [5, 1]`, `nums2 = [0, 0]`, `x = 6`
- Output: `0`
- Explanation: The initial sum already meets the requirement.
