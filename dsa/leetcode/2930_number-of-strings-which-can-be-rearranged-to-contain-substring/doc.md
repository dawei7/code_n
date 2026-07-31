# Number of Strings Which Can Be Rearranged to Contain Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2930 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/) |

## Problem Description

### Goal

A lowercase English string of length `n` is good when its characters can be
rearranged so that the resulting string contains `"leet"` as a substring. The
rearrangement may place unused characters anywhere; only the available
character multiplicities determine whether the four required letters can be
made contiguous in the necessary order.

Count all good strings of length `n`. Different original orderings are
different strings even when they have the same multiset of characters. Since
the count can be large, return it modulo $10^9+7$. A substring is a contiguous
sequence of characters.

### Function Contract

**Inputs**

- `n`: The length of every lowercase English string being counted.

The constraint is $1\le\texttt{n}\le10^5$.

**Return value**

- The number of length-`n` strings rearrangeable to contain `"leet"`, modulo
  $10^9+7$.

### Examples

**Example 1**

- Input: `n = 4`
- Output: `12`
- Explanation: A good four-character string must be one of the 12 distinct permutations of the multiset `{l, e, e, t}`.

**Example 2**

- Input: `n = 10`
- Output: `83943898`
- Explanation: There are `526083947580` good strings before applying the modulus.
