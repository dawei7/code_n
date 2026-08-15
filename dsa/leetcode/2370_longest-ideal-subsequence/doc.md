# Longest Ideal Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2370 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-ideal-subsequence/) |

## Problem Description

### Goal

Given a string `s` of lowercase English letters and an integer `k`, choose a subsequence `t`. Characters may be deleted from `s`, but the relative order of every retained character must remain unchanged.

The subsequence is ideal when the absolute difference between the alphabet positions of every adjacent pair in `t` is at most `k`. Alphabet order is not cyclic: the distance between `'a'` and `'z'` is $25$, not $1$. Return the greatest possible length of an ideal subsequence.

### Function Contract

**Inputs**

- `s`: A string of lowercase English letters with $1 \le \lvert\texttt{s}\rvert \le 10^5$.
- `k`: The maximum allowed alphabet-position difference between adjacent chosen letters, with $0 \le \texttt{k} \le 25$.

**Return value**

- Return the length of the longest ideal subsequence of `s`.

**Semantics**

- A subsequence keeps the original relative order but need not use contiguous positions.
- The adjacency restriction applies to neighboring letters in the chosen subsequence, even when other source characters were skipped.

### Examples

#### Example 1

- **Input:** `s = "acfgbd", k = 2`
- **Output:** `4`
- **Explanation:** `"acbd"` is an ideal subsequence. In contrast, keeping `'c'` next to `'f'` would create an alphabet distance of $3$.

#### Example 2

- **Input:** `s = "abcd", k = 3`
- **Output:** `4`
- **Explanation:** Every adjacent pair already satisfies the limit, so the complete string is ideal.
