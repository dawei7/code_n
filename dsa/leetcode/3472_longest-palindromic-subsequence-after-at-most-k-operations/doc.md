# Longest Palindromic Subsequence After at Most K Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3472 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/) |

## Problem Description

### Goal

You are given a lowercase English string `s` and an operation budget `k`. One operation replaces the character at any chosen position by its next or previous alphabet letter. The alphabet is cyclic: moving backward from `'a'` reaches `'z'`, and moving forward from `'z'` reaches `'a'`. A position may be changed repeatedly, and no more than `k` operations may be performed in total.

After making any permitted changes, choose a subsequence of the resulting string. A subsequence keeps the relative order of its selected positions but may omit any other positions. Return the maximum possible length of a palindromic subsequence, meaning one that reads identically from left to right and right to left. The transformed string itself and the chosen subsequence do not need to be returned.

### Function Contract

**Inputs**

- `s`: The lowercase English string whose characters may be changed.
- `k`: The maximum total number of single-letter cyclic changes.

Let $n=\lvert\texttt{s}\rvert$. The constraints are $1\le n\le200$ and $1\le k\le200$.

**Return value**

Return the greatest length of a palindromic subsequence obtainable after at most `k` operations.

### Examples

#### Example 1

- **Input:** `s = "abced", k = 2`
- **Output:** `3`

Changing `'b'` to `'c'` and `'d'` to `'c'` permits a palindromic subsequence of three `'c'` characters.

#### Example 2

- **Input:** `s = "aaazzz", k = 4`
- **Output:** `6`

Four cyclic changes are sufficient to make the full six-character string a palindrome.

#### Example 3

- **Input:** `s = "az", k = 1`
- **Output:** `2`

The two letters are adjacent across the alphabet boundary, so one operation can make them equal.
