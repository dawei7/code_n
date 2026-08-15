# Trionic Array I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3637 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/trionic-array-i/) |

## Problem Description

### Goal

Given an integer array `nums` of length $n$, determine whether two indices $p$ and $q$ exist with $0<p<q<n-1$ such that the entire array has exactly three consecutive monotonic segments.

The prefix from index 0 through $p$ must be strictly increasing. The segment from $p$ through $q$ must be strictly decreasing, and the suffix from $q$ through index $n-1$ must be strictly increasing. The turning-point values belong to both adjacent segments.

Return `true` when such breakpoints exist and `false` otherwise. Each phase must contain at least one comparison, and equal adjacent values satisfy neither strict direction.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $3 \le n \le 100$ and $-1000 \le \texttt{nums[i]} \le 1000$.

**Return value**

Return whether the whole array follows a nonempty strictly-increasing, then nonempty strictly-decreasing, then nonempty strictly-increasing pattern.

### Examples

#### Example 1

- **Input:** `nums = [1, 3, 5, 4, 2, 6]`
- **Output:** `true`
- **Explanation:** Choose $p=2$ and $q=4$ to obtain increasing `[1, 3, 5]`, decreasing `[5, 4, 2]`, and increasing `[2, 6]`.

#### Example 2

- **Input:** `nums = [2, 1, 3]`
- **Output:** `false`
- **Explanation:** No two legal interior breakpoints can provide all three required phases.
