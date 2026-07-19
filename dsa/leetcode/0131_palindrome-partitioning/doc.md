# Palindrome Partitioning

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 131 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-partitioning/) |

## Problem Description
### Goal
Given a nonempty string, place boundaries between characters to divide it into contiguous, nonempty substrings. A division is valid only when every resulting substring is a palindrome, meaning it reads identically from both ends.

Return every valid partition of the entire string. Each partition must preserve the original character order, use every character exactly once, and list its pieces from left to right. Different boundary placements count as different partitions even when repeated characters are present. The partitions may appear in any outer order, and splitting every character into a one-letter palindrome always provides at least one valid result.

### Function Contract
**Inputs**

- `s`: a nonempty lowercase string

**Return value**

All palindrome partitions. Outer partition order does not matter; substring order within each partition does.

### Examples
**Example 1**

- Input: `s = "aab"`
- Output: `[["a", "a", "b"], ["aa", "b"]]`

**Example 2**

- Input: `s = "a"`
- Output: `[["a"]]`

**Example 3**

- Input: `s = "efe"`
- Output: `[["e", "f", "e"], ["efe"]]`
