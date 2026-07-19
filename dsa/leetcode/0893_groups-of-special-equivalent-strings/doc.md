# Groups of Special-Equivalent Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 893 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/groups-of-special-equivalent-strings/) |

## Problem Description
### Goal
All strings in `words` have the same length. In one move on a string, choose any two even indices and swap their characters, or choose any two odd indices and swap their characters. Any number of moves may be performed.

Two strings are special-equivalent when these moves can transform one into the other. The array is partitioned into maximal non-empty groups whose members are pairwise special-equivalent. Return the number of such groups.

### Function Contract
Let $N=\lvert\texttt{words}\rvert$ and let $L$ be the common word length.

**Inputs**

- `words`: $N$ lowercase English strings of length $L$, where $1 \leq N \leq 1000$ and $1 \leq L \leq 20$.

**Return value**

Return the number of distinct special-equivalence groups represented in `words`.

### Examples
**Example 1**

- Input: `words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]`
- Output: `3`

The groups are `{"abcd","cdab","cbad"}`, `{"xyzz","zzxy"}`, and `{"zzyx"}`.

**Example 2**

- Input: `words = ["abc","acb","bac","bca","cab","cba"]`
- Output: `3`

**Example 3**

- Input: `words = ["aa","aa","aa"]`
- Output: `1`
