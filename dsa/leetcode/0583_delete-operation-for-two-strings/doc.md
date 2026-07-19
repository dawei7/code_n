# Delete Operation for Two Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 583 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/delete-operation-for-two-strings/) |

## Problem Description
### Goal
Given two strings `word1` and `word2`, make the strings the same using deletion steps. In one step, you may delete exactly one character from either string; remaining characters keep their relative order, and insertion, replacement, or reordering is not allowed.

Return the minimum number of steps required. Deletions may be split between the two strings in any way, and the common result may be empty when necessary, although retaining the longest possible shared subsequence minimizes the total number removed.

### Function Contract
**Inputs**

- `word1: str`: the first string
- `word2: str`: the second string

**Return value**

- The smallest number of deletions from both strings combined that leaves the same remaining string on each side

### Examples
**Example 1**

- Input: `word1 = "sea", word2 = "eat"`
- Output: `2`

**Example 2**

- Input: `word1 = "leetcode", word2 = "etco"`
- Output: `4`

**Example 3**

- Input: `word1 = "a", word2 = "b"`
- Output: `2`
