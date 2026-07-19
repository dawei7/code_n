# Contains Duplicate II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 219 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/contains-duplicate-ii/) |

## Problem Description
### Goal
Given an integer array `nums` and a nonnegative distance bound `k`, look for two distinct indices `i` and `j` that store equal values. In addition to value equality, their absolute index distance must satisfy $| i - j | \le k$.

Return `True` when at least one pair meets both conditions and `False` otherwise. Duplicate values farther apart than `k` do not qualify, and an occurrence cannot pair with itself even when `k` is zero. If a value occurs several times, any sufficiently close pair is enough; the function does not return the value, indices, or smallest distance.

### Function Contract
**Inputs**

- `nums`: an integer list
- `k`: maximum allowed index distance

**Return value**

`True` when a qualifying equal-value pair exists; otherwise `False`.

### Examples
**Example 1**

- Input: `[1,2,3,1], k = 3`
- Output: `True`

**Example 2**

- Input: `[1,2,3,1,2,3], k = 2`
- Output: `False`

**Example 3**

- Input: `[1,1], k = 0`
- Output: `False`
