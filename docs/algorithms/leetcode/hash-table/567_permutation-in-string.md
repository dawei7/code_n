# Permutation in String

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_40` |
| Frontend ID | 567 |
| Difficulty | Medium |
| Topics | Hash Table, Two Pointers, String, Sliding Window |
| Official Link | [permutation-in-string](https://leetcode.com/problems/permutation-in-string/) |

## Problem Description & Examples
### Goal
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### Function Contract
**Inputs**

- `n`: int - number of pairs

**Return value**

List[str] - all well-formed parentheses of n pairs

### Examples
**Example 1**

- Input: `n = 3`
- Output: `["((()))", "(()())", "(())()", "()(())", "()()()"]`

**Example 2**

- Input: `n = 1`
- Output: `['()']`

**Example 3**

- Input: `n = 2`
- Output: `['(())', '()()']`

---

## Underlying Base Algorithm(s)
- [Window with character state](hash_03_longest-substring-without-repeating.md)
- [Window frequency counting](hash_05_count-distinct-in-window.md)

---

## Complexity Analysis
- **Time Complexity**: `O(2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
