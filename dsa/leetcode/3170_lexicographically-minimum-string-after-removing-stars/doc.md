# Lexicographically Minimum String After Removing Stars

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3170 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Stack, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/) |

## Problem Description

### Goal

A string `s` contains lowercase English letters and possibly `*` characters. Remove every star by repeatedly selecting the leftmost remaining `*`, deleting it, and also deleting one smallest non-star character to its left. If that smallest character occurs more than once to the left of the star, any one of those occurrences may be chosen.

Return the lexicographically smallest string obtainable after all stars have been removed. The input guarantees that every star has an eligible letter to its left when it is processed.

### Function Contract

**Inputs**

- `s`: A string containing lowercase English letters and `*` characters.

Let $n = \lvert\texttt{s}\rvert$. The constraints satisfy $1 \le n \le 10^5$, and the sequence always permits all required deletions.

**Return value**

- The lexicographically smallest remaining string after applying every star operation.

### Examples

**Example 1**

- Input: `s = "aaba*"`
- Output: `"aab"`

The smallest eligible letter is `a`. Deleting its rightmost eligible occurrence gives the smallest remaining order.

**Example 2**

- Input: `s = "abc"`
- Output: `"abc"`

There are no stars, so no characters are removed.
