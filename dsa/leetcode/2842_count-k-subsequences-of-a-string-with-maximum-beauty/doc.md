# Count K-Subsequences of a String With Maximum Beauty

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2842 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, Math, String, Greedy, Sorting, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/) |

## Problem Description

### Goal

You are given a lowercase English string `s` and an integer `k`. A k-subsequence is a subsequence of length $k$ in which every selected character is unique. A subsequence keeps the selected indices in their original relative order, although any number of other positions may be omitted.

For a character $c$, let $f(c)$ be its total number of occurrences in the original string `s`. The beauty of a k-subsequence is the sum of $f(c)$ over its $k$ selected characters. Count the k-subsequences whose beauty is as large as possible, and return the count modulo $10^9+7$.

The frequencies are always taken from the complete input string, not from an individual subsequence. Two subsequences are different whenever their sets of selected indices differ, even if those selections spell the same string. If `s` contains fewer than $k$ distinct characters, no k-subsequence exists and the result is `0`.

### Function Contract

**Inputs**

- `s`: A string containing only lowercase English letters.
- `k`: The required number of pairwise distinct selected characters.

The constraints are $1\le\lvert\texttt{s}\rvert\le2\cdot10^5$ and $1\le k\le\lvert\texttt{s}\rvert$.

**Return value**

- The number of maximum-beauty k-subsequences, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `s = "bcca", k = 2`
- **Output:** `4`
- **Explanation:** The frequencies are $f(a)=1$, $f(b)=1$, and $f(c)=2$. Maximum beauty is $3$, and four different pairs of indices select `c` together with either `a` or `b`.

#### Example 2

- **Input:** `s = "abbcd", k = 4`
- **Output:** `2`
- **Explanation:** All four distinct characters must be chosen. Either occurrence of `b` can supply its character, producing two different subsequences with beauty $5$.
