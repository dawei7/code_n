# Edit Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_204` |
| Frontend ID | 72 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming |
| Official Link | [edit-distance](https://leetcode.com/problems/edit-distance/) |

## Problem Description & Examples
### Goal
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

### Function Contract
**Inputs**

- `word1`: str
- `word2`: str

**Return value**

int - minimum edit distance

### Examples
**Example 1**

- Input: `word1 = "horse", word2 = "ros"`
- Output: `3`

**Example 2**

- Input: `word1 = 'ac', word2 = 'ed'`
- Output: `2`

**Example 3**

- Input: `word1 = 'ca', word2 = 'dd'`
- Output: `2`

---

## Underlying Base Algorithm(s)
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
