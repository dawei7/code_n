# Construct Target Array With Multiple Sums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1354 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/construct-target-array-with-multiple-sums/) |

## Problem Description

### Goal

Begin with an array of the same length as `target` in which every value is `1`. In one operation, compute the sum of all current array values, choose any index, and replace the value at that index with the computed sum. All other positions remain unchanged.

Given a positive integer array `target`, determine whether some finite sequence of these operations can transform the all-ones array into exactly `target`. Return `true` when such a construction exists and `false` otherwise.

### Function Contract

**Inputs**

- `target`: a nonempty array of positive integers.
- Let $n$ be its length and $M$ be its maximum value.

**Return value**

- Return `true` exactly when `target` is reachable from an all-ones array under the sum-replacement operation.

### Examples

**Example 1**

- Input: `target = [9, 3, 5]`
- Output: `true`

**Example 2**

- Input: `target = [1, 1, 1, 2]`
- Output: `false`

**Example 3**

- Input: `target = [8, 5]`
- Output: `true`
