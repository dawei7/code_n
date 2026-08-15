# Make Number of Distinct Characters Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2531 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/make-number-of-distinct-characters-equal/) |

## Problem Description

### Goal

You are given two 0-indexed strings, `word1` and `word2`. One move chooses an index `i` in `word1` and an index `j` in `word2`, then swaps the two characters at those positions.

Determine whether exactly one such move can leave the two resulting strings with the same number of distinct characters. The chosen characters may be equal; in that case the required move is still performed even though neither string's contents change.

### Function Contract

**Inputs**

- `word1`: The first nonempty lowercase English string.
- `word2`: The second nonempty lowercase English string.

Each string has length between $1$ and $10^5$, inclusive.

**Return value**

Return `true` if some single cross-string character swap makes the distinct-character counts equal; otherwise return `false`.

### Examples

#### Example 1

- **Input:** `word1 = "ac", word2 = "b"`
- **Output:** `false`
- **Explanation:** Every swap leaves the first string with two distinct characters and the second with one.

#### Example 2

- **Input:** `word1 = "abcc", word2 = "aab"`
- **Output:** `true`
- **Explanation:** Swapping a `c` from the first string with an `a` from the second yields three distinct characters in each.

#### Example 3

- **Input:** `word1 = "abcde", word2 = "fghij"`
- **Output:** `true`
- **Explanation:** Swapping any pair preserves five distinct characters in both strings.
