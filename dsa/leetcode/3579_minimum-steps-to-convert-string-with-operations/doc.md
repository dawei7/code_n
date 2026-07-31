# Minimum Steps to Convert String with Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3579 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/) |

## Problem Description

### Goal

Two lowercase strings `word1` and `word2` have the same length. Divide `word1` into one or more non-empty contiguous substrings; these segments keep their order and correspond to the same index ranges in `word2`.

Within each chosen substring, an operation may replace one character with another lowercase letter, swap any two characters, or reverse the entire substring. Each operation costs one step. A character position may participate at most once in each operation type: at most one replacement, at most one swap, and at most one reversal.

Determine the minimum total steps needed to transform every segment of `word1` into its corresponding segment of `word2`, and therefore transform the complete first string into the second.

### Function Contract

**Inputs**

- `word1`: A lowercase English string of length $n$, where $1\le n\le100$.
- `word2`: A lowercase English string with the same length as `word1`.

**Return value**

Return the minimum number of allowed operations required to transform `word1` into `word2`.

### Examples

**Example 1**

- Input: `word1 = "abcdf", word2 = "dacbe"`
- Output: `4`
- Explanation: One optimal partition uses `"ab"`, `"c"`, and `"df"`; reversing and replacing within the first segment and making two replacements in the last costs four steps.

**Example 2**

- Input: `word1 = "abceded", word2 = "baecfef"`
- Output: `4`
- Explanation: Partitioning as `"ab"`, `"ce"`, and `"ded"` permits two swaps followed by two replacements.

**Example 3**

- Input: `word1 = "abcdef", word2 = "fedabc"`
- Output: `2`
- Explanation: Reverse the complete string, then use one swap to obtain the target.

---
