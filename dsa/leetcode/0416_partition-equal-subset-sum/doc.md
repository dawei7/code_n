# Partition Equal Subset Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 416 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/) |

## Problem Description
### Goal
Given a nonempty array of positive integers, divide its element occurrences into two disjoint subsets. Every array position must belong to exactly one subset, and duplicate values at different positions remain separate selectable occurrences.

Return `True` when the two subset sums can be equal and `False` otherwise. This is equivalent to finding one subset totaling half the complete array sum, which is impossible when that total is odd. Subsets do not need to correspond to contiguous positions or have equal cardinality. The function returns only feasibility, not the two partitions themselves.

### Function Contract
**Inputs**

- `nums`: a nonempty array of positive integers

**Return value**

- Return `True` when some subset sums to half of the array total; otherwise return `False`.

### Examples
**Example 1**

- Input: `nums = [1,5,11,5]`
- Output: `True`

**Example 2**

- Input: `nums = [1,2,3,5]`
- Output: `False`

**Example 3**

- Input: `nums = [2,2,1,1]`
- Output: `True`
