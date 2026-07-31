# Partition Array According to Given Pivot

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2161 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/partition-array-according-to-given-pivot/) |

## Problem Description

### Goal

Given a 0-indexed integer array `nums` and an integer `pivot`, rearrange all
values into three consecutive groups. Every value smaller than `pivot` must
come first, every value equal to `pivot` must follow, and every value greater
than `pivot` must come last.

The rearrangement must be stable for values on either side of the pivot: if
two smaller values appeared in one order in `nums`, they must retain that
order in the result, and the same rule applies to two greater values. Return
the rearranged array. The pivot is guaranteed to occur at least once.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 10^5$ and every
  value lies from $-10^6$ through $10^6$.
- `pivot`: an integer that occurs in `nums`.

**Return value**

The stable three-way partition of `nums` around `pivot`.

### Examples

**Example 1**

- Input: `nums = [9, 12, 5, 10, 14, 3, 10]`, `pivot = 10`
- Output: `[9, 5, 3, 10, 10, 12, 14]`
- Explanation: The smaller subsequence remains `[9, 5, 3]` and the greater
  subsequence remains `[12, 14]`.

**Example 2**

- Input: `nums = [-3, 4, 3, 2]`, `pivot = 2`
- Output: `[-3, 2, 4, 3]`
- Explanation: The greater values retain their original order `[4, 3]`.
