# Longest String Chain

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1048 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Two Pointers, String, Dynamic Programming, Sorting |
| Official Link | [longest-string-chain](https://leetcode.com/problems/longest-string-chain/) |

## Problem Description & Examples
### Goal
Given a list of words, find the longest chain where each next word can be formed by inserting exactly one character into the previous word.

### Function Contract
**Inputs**

- `words`: List[str]

**Return value**

int - maximum chain length

### Examples
**Example 1**

- Input: `words = ["a", "b", "ba", "bca", "bda", "bdca"]`
- Output: `4`

**Example 2**

- Input: `words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]`
- Output: `5`

**Example 3**

- Input: `words = ["abcd", "dbqca"]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Dynamic programming over words sorted by length.

---

## Complexity Analysis
- **Time Complexity**: `O(n * L^2)` where `L` is max word length
- **Space Complexity**: `O(n)`
