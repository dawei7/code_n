# Shortest Subarray With OR at Least K II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3097 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [shortest-subarray-with-or-at-least-k-ii](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/) |

## Problem Description

### Goal

You are given an array `nums` of non-negative integers and a non-negative integer `k`. A subarray consists of one or more contiguous elements of `nums`. Such a non-empty subarray is *special* when the bitwise OR of all its elements is at least `k`.

Return the length of the shortest special subarray of `nums`. If no non-empty subarray has a bitwise OR of at least `k`, return `-1`.

### Function Contract

**Inputs**

- `nums`: A list of $n$ non-negative integers, where $1 \le n \le 2 \cdot 10^5$ and every value is at most $10^9$.
- `k`: The non-negative target threshold, with $0 \le k \le 10^9$.

Let

$$
V = \max\bigl(\{1, k\} \cup \{x : x \in \texttt{nums}\}\bigr).
$$

Thus, $O(\log V)$ bit positions suffice to represent every relevant value.

**Return value**

- The minimum positive length of a contiguous subarray whose bitwise OR is at least `k`, or `-1` if no such subarray exists.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3], k = 2`
- **Output:** `1`
- **Explanation:** The one-element subarray `[3]` has bitwise OR $3$, which reaches the threshold.

#### Example 2

- **Input:** `nums = [2, 1, 8], k = 10`
- **Output:** `3`
- **Explanation:** The entire array has bitwise OR $11$, and neither a one- nor a two-element subarray reaches $10$.

#### Example 3

- **Input:** `nums = [1, 2], k = 0`
- **Output:** `1`
- **Explanation:** Every non-empty subarray has a non-negative OR value, so one element is sufficient.
