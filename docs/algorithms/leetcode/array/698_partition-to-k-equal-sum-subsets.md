# Partition to K Equal Sum Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_135` |
| Frontend ID | 698 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask |
| Official Link | [partition-to-k-equal-sum-subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) |

## Problem Description & Examples
### Goal
Given an integer array `nums` and an integer `k`, return `True` if it is possible to divide this array into `k` non-empty subsets whose sums are all equal.

### Function Contract
**Inputs**

- `nums`: List[int]
- `k`: int

**Return value**

bool - True if partition exists

### Examples
**Example 1**

- Input: `nums = [4, 3, 2, 3, 5, 2, 1], k = 4`
- Output: `True`

**Example 2**

- Input: `nums = [4, 1, 3], k = 3`
- Output: `False`

**Example 3**

- Input: `nums = [3, 1], k = 2`
- Output: `False`

---

## Underlying Base Algorithm(s)
- [Permutations](backtrack_02_permutations.md)
- [Combination sum](backtrack_03_combination-sum.md)
- [Word break decision](backtrack_04_word-break-decision.md)

---

## Complexity Analysis
- **Time Complexity**: `O(2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
