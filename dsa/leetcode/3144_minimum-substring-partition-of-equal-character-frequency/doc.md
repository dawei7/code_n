# Minimum Substring Partition of Equal Character Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3144 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Dynamic Programming, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/) |

## Problem Description

### Goal

You are given a lowercase string `s`. Partition all of its characters, without reordering them, into one or more contiguous substrings.

A substring is balanced when every distinct character appearing in it occurs the same number of times. Cuts may be placed between any adjacent characters, and every resulting part must be balanced. Return the minimum number of balanced substrings needed to cover `s` completely.

### Function Contract

**Inputs**

- `s`: A nonempty string consisting only of lowercase English letters.

Let $n = \lvert\texttt{s}\rvert$. The constraint is $1 \le n \le 1000$.

**Return value**

Return the smallest number of contiguous balanced substrings whose concatenation is exactly `s`.

### Examples

#### Example 1

- **Input:** `s = "fabccddg"`
- **Output:** `3`
- **Explanation:** One minimum partition is `"fab"`, `"ccdd"`, and `"g"`; within each part, every character present has one common frequency.

#### Example 2

- **Input:** `s = "abababaccddb"`
- **Output:** `2`
- **Explanation:** The string can be split into the two balanced substrings `"abab"` and `"abaccddb"`.
