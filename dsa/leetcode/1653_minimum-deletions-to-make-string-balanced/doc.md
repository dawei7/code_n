# Minimum Deletions to Make String Balanced

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1653 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/) |

## Problem Description
### Goal
Given a string `s` containing only `a` and `b`, delete as few characters as possible so that it becomes balanced. A balanced string has no earlier `b` followed by a later `a`; equivalently, every remaining `a` appears before every remaining `b`.

Any number of characters may be deleted, including none. Deletions preserve the relative order of the characters that remain. Return only the minimum deletion count.

### Function Contract
**Inputs**

- `s`: a string of length $n$ containing only `a` and `b`, where $1 \le n \le 10^5$.

**Return value**

Return the minimum number of deletions needed to leave a string with no index pair $i<j$ such that `s[i] == "b"` and `s[j] == "a"`.

### Examples
**Example 1**

- Input: `s = "aababbab"`
- Output: `2`

Deleting two conflicting characters can leave either `aaabbb` or `aabbbb`.

**Example 2**

- Input: `s = "bbaaaaabb"`
- Output: `2`

Deleting the first two `b` characters leaves all `a` characters before the final `b` characters.

**Example 3**

- Input: `s = "abab"`
- Output: `1`

Removing the middle `b` leaves `aab`.
