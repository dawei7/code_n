# Shortest Common Supersequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1092 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/shortest-common-supersequence/) |

## Problem Description

### Goal

Given two lowercase English strings `str1` and `str2`, find the shortest string that contains both inputs as subsequences. A string is a subsequence of another when deleting zero or more characters from the latter leaves the former, without changing the order of retained characters.

Return any shortest common supersequence. More than one string can have the minimum length, and no lexicographic tie-breaking rule is required; the result only needs to preserve both input sequences and be as short as possible.

### Function Contract

**Inputs**

- `str1`: a lowercase English string of length $m$, where $1 \le m \le 1000$.
- `str2`: a lowercase English string of length $n$, where $1 \le n \le 1000$.

**Return value**

- Any minimum-length string containing both `str1` and `str2` as subsequences.

### Examples

**Example 1**

- Input: `str1 = "abac"`, `str2 = "cab"`
- Output: `"cabac"`

Deleting the first `c` leaves `"abac"`, while deleting the final `"ac"` leaves `"cab"`.

**Example 2**

- Input: `str1 = "aaaaaaaa"`, `str2 = "aaaaaaaa"`
- Output: `"aaaaaaaa"`
