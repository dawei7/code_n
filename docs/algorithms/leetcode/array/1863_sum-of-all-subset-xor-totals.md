# Sum of All Subset XOR Totals

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_123` |
| Frontend ID | 1863 |
| Difficulty | Easy |
| Topics | Array, Math, Backtracking, Bit Manipulation, Combinatorics, Enumeration |
| Official Link | [sum-of-all-subset-xor-totals](https://leetcode.com/problems/sum-of-all-subset-xor-totals/) |

## Problem Description & Examples
### Goal
Given an array `nums`, return the sum of all subset XOR totals. The XOR total of an array is the bitwise XOR of all its elements, or 0 if it is empty.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

int - sum of all subset XOR totals

### Examples
**Example 1**

- Input: `nums = [1, 3]`
- Output: `6`

**Example 2**

- Input: `nums = [5]`
- Output: `5`

**Example 3**

- Input: `nums = [1, 2, 3]`
- Output: `12`

---

## Underlying Base Algorithm(s)
- [Permutations](backtrack_02_permutations.md)
- [Combination sum](backtrack_03_combination-sum.md)
- [Word break decision](backtrack_04_word-break-decision.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
