# Longest Unequal Adjacent Groups Subsequence II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2901 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/) |

## Problem Description

### Goal

You are given an array of distinct strings `words` and an integer array `groups` of the same length $n$. The Hamming distance between two equal-length strings is the number of positions at which their characters differ.

Choose a longest subsequence of indices from $[0,1,\ldots,n-1]`. For every two consecutive selected indices $a<b$, their group values must be unequal, their words must have equal length, and the Hamming distance between `words[a]` and `words[b]` must be exactly $1$.

Return the corresponding selected words in index order. The input words may have different lengths, and if several longest subsequences exist, any one of them is valid.

### Function Contract

**Inputs**

- `words`: An array of pairwise distinct lowercase strings.
- `groups`: An array of positive group identifiers aligned with `words`.

The shared bounds are $1\le n\le1000$, $1\le\texttt{groups[i]}\le n$, and $1\le\lvert\texttt{words[i]}\rvert\le10$. Let $L=\max_i\lvert\texttt{words[i]}\rvert$.

**Return value**

Return any maximum-length word subsequence satisfying all adjacent group, length, and Hamming-distance conditions.

### Examples

**Example 1**

- Input: `words = ["bab", "dab", "cab"], groups = [1, 2, 2]`
- Output: `["bab", "dab"]`
- Explanation: The group identifiers differ and the equal-length words differ only at their first character. Choosing `"cab"` instead of `"dab"` is another valid longest answer.

**Example 2**

- Input: `words = ["a", "b", "c", "d"], groups = [1, 2, 3, 4]`
- Output: `["a", "b", "c", "d"]`
- Explanation: Every adjacent pair has different group identifiers, and every pair of distinct one-character words has Hamming distance $1$.
