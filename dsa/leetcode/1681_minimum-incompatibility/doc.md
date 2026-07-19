# Minimum Incompatibility

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1681 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-incompatibility/) |

## Problem Description
### Goal

Distribute every element of `nums` into exactly `k` subsets of equal size. Elements are occurrences, so equal values at different indices are distinct items; however, no one subset may contain two equal values. The order of elements within a subset and the order of the subsets themselves are irrelevant.

The incompatibility of one subset is its maximum value minus its minimum value. Minimize the sum of this quantity over all `k` subsets. Return that minimum total when a valid distribution exists, or `-1` when the multiplicities make it impossible to satisfy the distinct-values rule in every subset.

### Function Contract
**Inputs**

- `nums`: a list of $n$ integers, where $n \le 16$ and each value lies from $1$ through $n$
- `k`: the number of required subsets, with $1 \le k \le n$ and $n$ divisible by `k`

Let $m = n/k$ be the required number of elements in each subset.

**Return value**

The minimum possible sum of the `k` subset incompatibilities, or `-1` if no valid partition exists.

### Examples
**Example 1**

- Input: `nums = [1,2,1,4], k = 2`
- Output: `4`

**Example 2**

- Input: `nums = [6,3,8,1,3,1,2,2], k = 4`
- Output: `6`

**Example 3**

- Input: `nums = [5,3,3,6,3,3], k = 3`
- Output: `-1`
