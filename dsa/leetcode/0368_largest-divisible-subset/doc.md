# Largest Divisible Subset

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 368 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-divisible-subset/) |

## Problem Description
### Goal
Given a nonempty list of unique positive integers, choose a subset in which every pair is comparable by divisibility. For any two selected values `a` and `b`, either `a` divides `b` exactly or `b` divides `a` exactly.

Return any qualifying subset having maximum possible cardinality, with values in any order. Selection does not need to preserve original positions, and several maximum subsets may exist. Include each input value at most once. Pairwise divisibility across the complete subset is required; merely finding adjacent divisible pairs in an arbitrary ordering is insufficient unless they form a consistent divisibility chain.

### Function Contract
**Inputs**

- `nums`: a non-empty list of distinct positive integers

**Return value**

- Any largest subset of `nums` whose every pair is comparable by divisibility. The values may be returned in any order.

### Examples
**Example 1**

- Input: `nums = [1,2,3]`
- Output: `[1,2]`

**Example 2**

- Input: `nums = [1,2,4,8]`
- Output: `[1,2,4,8]`

**Example 3**

- Input: `nums = [3,4,16,8]`
- Output: `[4,8,16]`
