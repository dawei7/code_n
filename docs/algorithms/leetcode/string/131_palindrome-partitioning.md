# Palindrome Partitioning

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_132` |
| Frontend ID | 131 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming, Backtracking |
| Official Link | [palindrome-partitioning](https://leetcode.com/problems/palindrome-partitioning/) |

## Problem Description & Examples
### Goal
Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

### Function Contract
**Inputs**

- `s`: str

**Return value**

List[List[str]] - all possible partitions of palindromes

### Examples
**Example 1**

- Input: `s = "aab"`
- Output: `[["a", "a", "b"], ["aa", "b"]]`

**Example 2**

- Input: `s = 'cc'`
- Output: `[['c', 'c'], ['cc']]`

**Example 3**

- Input: `s = 'ac'`
- Output: `[['a', 'c']]`

---

## Underlying Base Algorithm(s)
- [Permutations](backtrack_02_permutations.md)
- [Combination sum](backtrack_03_combination-sum.md)
- [Word break decision](backtrack_04_word-break-decision.md)

---

## Complexity Analysis
- **Time Complexity**: `O(2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
