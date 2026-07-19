# Can Make Arithmetic Progression From Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1502 |
| Difficulty | Easy |
| Topics | Array, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/) |

## Problem Description
### Goal

An arithmetic progression is a sequence in which the difference between every pair of consecutive elements is the same. The common difference may be positive, negative, or zero; only equality across all adjacent differences matters.

Given an integer array `arr`, determine whether its elements can be rearranged so that the resulting sequence is an arithmetic progression. Every array occurrence must be used exactly once. Return `true` when at least one such ordering exists and `false` otherwise; the input order itself does not need to satisfy the progression.

### Function Contract
**Inputs**

Let $n=\lvert\texttt{arr}\rvert$.

- `arr`: an integer array with $2 \le n \le 1000$.
- Every value lies in $[-10^6,10^6]$.
- Values need not be distinct and may arrive in any order.

**Return value**

Return `true` if all $n$ occurrences can be reordered into a sequence with one constant adjacent difference. Otherwise return `false`. The app-local implementation does not mutate `arr`.

### Examples
**Example 1**

- Input: `arr = [3,5,1]`
- Output: `true`
- Explanation: Reordering to `[1,3,5]` gives common difference $2$; reversing that order gives common difference $-2$.

**Example 2**

- Input: `arr = [1,2,4]`
- Output: `false`
- Explanation: No ordering of these three values has equal adjacent differences.

**Example 3**

- Input: `arr = [7,7,7]`
- Output: `true`
- Explanation: Every adjacent difference is zero.
